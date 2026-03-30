"""
Read a PST file and print extracted email summaries plus contact details,
or compose a draft email and save as MSG/EML and optionally add it to a PST Drafts folder.

Requires: pip install Aspose.Email-for-Python-via-NET
See: https://docs.aspose.com/email/python-net/working-with-messages-in-a-pst-file/
     https://blog.aspose.com/email/parse-outlook-pst-files-in-python/

Place your sample PST as xxx.pst next to this script, or pass --pst path.
Optional: set ASPOSE_EMAIL_LICENSE_PATH to a .lic file to remove evaluation limits.

Commands (first argument optional for backward compatibility — omitted implies "extract"):
  python extract_pst_emails_and_contacts.py extract --pst xxx.pst
  python extract_pst_emails_and_contacts.py draft --subject "Hi" --to you@example.com --out draft.msg
  python extract_pst_emails_and_contacts.py draft --subject "Hi" --to you@example.com --append-to-pst xxx.pst
"""

import argparse
import contextlib
import io
import os
import sys
from typing import List, Optional

from aspose.email import MailAddress, MailMessage
from aspose.email.mapi import MailConversionOptions, MapiContact, MapiMessage, MapiMessageFlags
from aspose.email.storage.pst import PersonalStorage, StandardIpmFolder


def _apply_license(path: Optional[str]) -> None:
    if not path:
        return
    try:
        from aspose.email import License

        lic = License()
        lic.set_license(path)
    except Exception as ex:
        print(f"Warning: could not apply license file {path!r}: {ex}", file=sys.stderr)


def _safe_str(value) -> str:
    if value is None:
        return ""
    return str(value)


def _truncate(text: str, max_len: int) -> str:
    text = text.replace("\r\n", "\n").strip()
    if len(text) <= max_len:
        return text
    return text[: max_len - 3] + "..."


def print_contact_from_message(mapi: MapiMessage) -> None:
    item = mapi.to_mapi_message_item()
    if not isinstance(item, MapiContact):
        print(f"    (not a MapiContact wrapper; message_class={_safe_str(mapi.message_class)})")
        return

    c: MapiContact = item
    print(f"    Display name: {_safe_str(c.display_name)}")
    if c.name_info:
        ni = c.name_info
        print(
            "    Name: "
            f"{_safe_str(ni.given_name)} {_safe_str(ni.middle_name)} {_safe_str(ni.surname)}".strip()
        )
    if c.professional_info and c.professional_info.company_name:
        print(f"    Company: {_safe_str(c.professional_info.company_name)}")
    if c.professional_info and c.professional_info.job_title:
        print(f"    Title: {_safe_str(c.professional_info.job_title)}")
    ea = c.electronic_addresses
    if ea:
        for label, addr in (
            ("Email1", ea.email1),
            ("Email2", ea.email2),
            ("Email3", ea.email3),
        ):
            if addr and getattr(addr, "address", None):
                print(f"    {label}: {_safe_str(addr.address)}")
    t = c.telephones
    if t:
        if getattr(t, "business_telephone_number", None):
            print(f"    Business phone: {_safe_str(t.business_telephone_number)}")
        if getattr(t, "mobile_telephone_number", None):
            print(f"    Mobile: {_safe_str(t.mobile_telephone_number)}")
        if getattr(t, "home_telephone_number", None):
            print(f"    Home: {_safe_str(t.home_telephone_number)}")


def extract_contacts(pst: PersonalStorage, max_items: Optional[int]) -> int:
    folder = pst.get_predefined_folder(StandardIpmFolder.CONTACTS)
    if folder is None:
        print("No predefined Contacts folder in this PST.")
        return 0

    print(f"\n=== Contacts ({folder.display_name}) ===\n")
    count = 0
    for message_info in folder.get_contents():
        if max_items is not None and count >= max_items:
            print(f"... stopped after {max_items} contacts (--max-contacts)")
            break
        try:
            mapi = pst.extract_message(message_info)
        except Exception as ex:
            print(f"  [skip entry_id={message_info.entry_id_string}] {ex}")
            continue
        print(f"  Contact #{count + 1}: {_safe_str(message_info.subject)}")
        print_contact_from_message(mapi)
        print()
        count += 1
    return count


def _is_likely_mail(mapi: MapiMessage) -> bool:
    mc = _safe_str(mapi.message_class).upper()
    if not mc:
        return True
    if "IPM.CONTACT" in mc:
        return False
    return True


def _split_addresses(s: Optional[str]) -> List[str]:
    if not s or not str(s).strip():
        return []
    return [p.strip() for p in str(s).split(",") if p.strip()]


def build_draft_mapi_message(
    subject: str,
    body: str,
    to_addrs: List[str],
    cc_addrs: List[str],
    bcc_addrs: List[str],
    from_addr: Optional[str],
) -> MapiMessage:
    """Create an unsent (draft) MapiMessage — same idea as SavingMessageInDraftStatus / CreatingAndSavingOutlookMSG."""
    eml = MailMessage()
    eml.is_draft = True
    eml.subject = subject or ""
    eml.body = body or ""

    if from_addr:
        eml.from_address = MailAddress(from_addr)

    for a in to_addrs:
        eml.to.append(MailAddress(a))
    for a in cc_addrs:
        eml.cc.append(MailAddress(a))
    for a in bcc_addrs:
        eml.bcc.append(MailAddress(a))

    mapi = MapiMessage.from_mail_message(eml)
    mapi.set_message_flags(MapiMessageFlags.UNSENT)
    return mapi


def save_draft(
    mapi: MapiMessage,
    out_path: str,
    fmt: str,
) -> None:
    fmt = fmt.lower()
    if fmt == "msg":
        mapi.save(out_path)
        return
    if fmt == "eml":
        eml = mapi.to_mail_message(MailConversionOptions())
        eml.save(out_path)
        return
    raise ValueError(f"Unknown format: {fmt!r} (use msg or eml)")


def append_draft_to_pst(pst_path: str, mapi: MapiMessage) -> None:
    """Add the draft to the PST Drafts folder (writable open)."""
    with PersonalStorage.from_file(pst_path, True) as pst:
        drafts = pst.get_predefined_folder(StandardIpmFolder.DRAFTS)
        if drafts is None:
            drafts = pst.create_predefined_folder("Drafts", StandardIpmFolder.DRAFTS)
        drafts.add_message(mapi)


def run_draft(
    subject: str,
    body: str,
    body_file: Optional[str],
    to_s: str,
    cc_s: Optional[str],
    bcc_s: Optional[str],
    from_addr: Optional[str],
    out_path: Optional[str],
    fmt: str,
    append_to_pst: Optional[str],
) -> None:
    _apply_license(os.environ.get("ASPOSE_EMAIL_LICENSE_PATH"))

    text = body or ""
    if body_file:
        with open(body_file, encoding="utf-8", errors="replace") as f:
            text = f.read()

    to_addrs = _split_addresses(to_s)
    cc_addrs = _split_addresses(cc_s)
    bcc_addrs = _split_addresses(bcc_s)

    mapi = build_draft_mapi_message(subject, text, to_addrs, cc_addrs, bcc_addrs, from_addr)

    if out_path:
        save_draft(mapi, out_path, fmt)
        print(f"Saved draft ({fmt.upper()}): {out_path}")

    if append_to_pst:
        if not os.path.isfile(append_to_pst):
            raise FileNotFoundError(f"PST not found: {append_to_pst}")
        append_draft_to_pst(append_to_pst, mapi)
        print(f"Added draft to Drafts in: {append_to_pst}")

    if not out_path and not append_to_pst:
        raise ValueError(
            "Specify --out path and/or --append-to-pst so the draft is saved somewhere."
        )


def walk_and_print_emails(
    pst: PersonalStorage,
    folder,
    max_items: Optional[int],
    printed: List[int],
) -> None:
    """Recursively walk folders; print mail-like items (skips IPM.Contact)."""
    name = _safe_str(folder.display_name)
    try:
        messages = folder.get_contents()
    except Exception as ex:
        print(f"[Folder {name}] could not list contents: {ex}")
        return

    for message_info in messages:
        if max_items is not None and printed[0] >= max_items:
            return
        try:
            mapi = pst.extract_message(message_info)
        except Exception as ex:
            print(f"  [skip {name} / {message_info.entry_id_string}] {ex}")
            continue
        if not _is_likely_mail(mapi):
            continue

        printed[0] += 1
        print(f"--- Email #{printed[0]} — folder: {name} — {_safe_str(message_info.subject)} ---")
        print(f"From: {_safe_str(mapi.sender_name)} <{_safe_str(mapi.sender_email_address)}>")
        print(f"To: {_safe_str(mapi.display_to)}")
        if _safe_str(mapi.display_cc):
            print(f"Cc: {_safe_str(mapi.display_cc)}")
        print(f"Date: {_safe_str(mapi.delivery_time)}")
        body = _safe_str(mapi.body)
        if body:
            print(f"Body:\n{_truncate(body, 500)}")
        print()

    if folder.has_sub_folders:
        for sub in folder.get_sub_folders():
            walk_and_print_emails(pst, sub, max_items, printed)
            if max_items is not None and printed[0] >= max_items:
                return


def run(pst_path: str, max_emails: Optional[int], max_contacts: Optional[int]) -> None:
    if not os.path.isfile(pst_path):
        raise FileNotFoundError(f"PST not found: {pst_path}")

    _apply_license(os.environ.get("ASPOSE_EMAIL_LICENSE_PATH"))

    with PersonalStorage.from_file(pst_path, False) as pst:
        print(f"Opened: {pst_path}")
        store = pst.store
        if store and getattr(store, "display_name", None):
            print(f"Store: {_safe_str(store.display_name)}")

        extract_contacts(pst, max_contacts)

        print("\n=== Emails (all folders; IPM.Contact items skipped) ===\n")
        printed = [0]
        walk_and_print_emails(pst, pst.root_folder, max_emails, printed)
        if max_emails is not None and printed[0] >= max_emails:
            print(f"... stopped after {max_emails} emails (--max-emails)")


def run_extract_to_string(
    pst_path: str,
    max_emails: Optional[int] = None,
    max_contacts: Optional[int] = None,
) -> str:
    """Run extract and return printed report (for MCP / programmatic use)."""
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        run(pst_path, max_emails, max_contacts)
    return buf.getvalue()


def run_draft_to_string(
    subject: str,
    body: str,
    body_file: Optional[str],
    to_s: str,
    cc_s: Optional[str],
    bcc_s: Optional[str],
    from_addr: Optional[str],
    out_path: Optional[str],
    fmt: str,
    append_to_pst: Optional[str],
) -> str:
    """Run draft creation and return printed status lines (for MCP / programmatic use)."""
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        run_draft(
            subject=subject,
            body=body,
            body_file=body_file,
            to_s=to_s,
            cc_s=cc_s,
            bcc_s=bcc_s,
            from_addr=from_addr,
            out_path=out_path,
            fmt=fmt,
            append_to_pst=append_to_pst,
        )
    return buf.getvalue()


def main() -> None:
    # Backward compatibility: `python script.py --pst ...` → implicit `extract`
    if len(sys.argv) > 1 and sys.argv[1] not in (
        "extract",
        "draft",
        "-h",
        "--help",
    ):
        sys.argv.insert(1, "extract")

    here = os.path.dirname(os.path.abspath(__file__))
    default_pst = os.path.join(here, "xxx.pst")
    parser = argparse.ArgumentParser(
        description="Extract emails/contacts from a PST, or create draft messages (MSG/EML / PST Drafts)."
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_ext = sub.add_parser("extract", help="list contacts and mail from a PST")
    p_ext.add_argument(
        "--pst",
        default=default_pst,
        help=f"path to .pst file (default: {default_pst})",
    )
    p_ext.add_argument(
        "--max-emails",
        type=int,
        default=None,
        metavar="N",
        help="stop after N email-like messages (default: no limit)",
    )
    p_ext.add_argument(
        "--max-contacts",
        type=int,
        default=None,
        metavar="N",
        help="stop after N contacts (default: no limit)",
    )

    p_draft = sub.add_parser("draft", help="compose an unsent draft (save MSG/EML and/or add to PST Drafts)")
    p_draft.add_argument("--subject", default="", help="message subject")
    p_draft.add_argument("--body", default="", help="plain-text body (use --body-file for long text)")
    p_draft.add_argument(
        "--body-file",
        default=None,
        metavar="PATH",
        help="read body from a UTF-8 file (overrides --body)",
    )
    p_draft.add_argument(
        "--to",
        default="",
        help="comma-separated To addresses",
    )
    p_draft.add_argument("--cc", default="", help="comma-separated Cc addresses")
    p_draft.add_argument("--bcc", default="", help="comma-separated Bcc addresses")
    p_draft.add_argument("--from", dest="from_addr", default=None, help="From address")
    p_draft.add_argument(
        "--out",
        default=None,
        metavar="PATH",
        help="save draft to this file (extension should match --format: .msg or .eml)",
    )
    p_draft.add_argument(
        "--format",
        choices=("msg", "eml"),
        default="msg",
        help="file format when using --out (default: msg)",
    )
    p_draft.add_argument(
        "--append-to-pst",
        default=None,
        metavar="PATH",
        help="add the draft to the Drafts folder of this PST (opens PST for writing)",
    )

    args = parser.parse_args()

    try:
        if args.command == "extract":
            run(args.pst, args.max_emails, args.max_contacts)
        else:
            if args.out is None and args.append_to_pst is None:
                parser.error("draft: specify --out and/or --append-to-pst")

            run_draft(
                subject=args.subject,
                body=args.body,
                body_file=args.body_file,
                to_s=args.to,
                cc_s=args.cc or None,
                bcc_s=args.bcc or None,
                from_addr=args.from_addr,
                out_path=args.out,
                fmt=args.format,
                append_to_pst=args.append_to_pst,
            )
    except FileNotFoundError as e:
        print(e, file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
