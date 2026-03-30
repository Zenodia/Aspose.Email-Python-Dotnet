"""
MCP server exposing PST extract + draft operations (FastMCP, streamable HTTP).

Depends on: pip install fastmcp python-dotenv
            plus Aspose.Email-for-Python-via-NET (same as extract_pst_emails_and_contacts.py)

Run:
  python extract_pst_mcp_server.py

Default URL: http://0.0.0.0:9001/mcp  (override with env if your FastMCP version supports it)

Environment:
  ASPOSE_EMAIL_LICENSE_PATH — optional .lic file
"""

from __future__ import annotations

import asyncio
import os
import sys
from pathlib import Path
from typing import Optional

_EXAMPLES = Path(__file__).resolve().parent
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

from fastmcp import FastMCP

import extract_pst_emails_and_contacts as pst

mcp = FastMCP("ExtractPstMCP")


@mcp.tool()
async def extract_pst(
    pst_path: str ,
    max_emails: Optional[int] = None,
    max_contacts: Optional[int] = None,
) -> str:
    """Extract contacts and mail-like messages from an Outlook PST file.

    Args:
        pst_path: Absolute or server-relative path to the .pst file on the machine running this server.
        max_emails: If set, stop after this many email-like items (default: no limit).
        max_contacts: If set, stop after this many contacts (default: no limit).

    Returns:
        Text report (same content as the CLI extract command prints).
    """
    pst_path= pst_path if pst_path is not None else"/home/ubuntu/OpenShellOpenClawMCP/Aspose.Email-Python-Dotnet/Examples/outlook.pst"
    try:
        return await asyncio.to_thread(
            pst.run_extract_to_string,
            pst_path,
            max_emails,
            max_contacts,
        )
    except Exception as ex:
        return f"Error: {type(ex).__name__}: {ex}"


@mcp.tool()
async def draft_email(
    subject: str = "",
    body: str = "",
    to_addresses: str = "",
    cc_addresses: str = "",
    bcc_addresses: str = "",
    from_address: Optional[str] = None,
    body_file: Optional[str] = None,
    out_path: Optional[str] = None,
    file_format: str = "msg",
    append_to_pst: Optional[str] = None,
) -> str:
    """Create an unsent draft (MSG/EML file and/or add to PST Drafts folder).

    Args:
        subject: Message subject.
        body: Plain-text body (ignored if body_file is set).
        to_addresses: Comma-separated To addresses.
        cc_addresses: Comma-separated Cc addresses.
        bcc_addresses: Comma-separated Bcc addresses.
        from_address: Optional From address.
        body_file: Optional UTF-8 file path on the server to use as body (overrides body).
        out_path: Save draft to this path (.msg or .eml per file_format).
        file_format: \"msg\" or \"eml\" when out_path is set.
        append_to_pst: If set, also add the draft to this PST's Drafts folder (PST opened writable).

    Returns:
        Status text from the operation.

    Note:
        You must set at least one of out_path or append_to_pst.
    """
    if not out_path and not append_to_pst:
        return (
            "Error: ValueError: specify at least one of out_path or append_to_pst "
            "so the draft is saved or added to a PST."
        )
    fmt = (file_format or "msg").lower()
    if fmt not in ("msg", "eml"):
        return f"Error: file_format must be msg or eml, got {file_format!r}"

    try:
        return await asyncio.to_thread(
            pst.run_draft_to_string,
            subject,
            body,
            body_file,
            to_addresses,
            cc_addresses or None,
            bcc_addresses or None,
            from_address,
            out_path,
            fmt,
            append_to_pst,
        )
    except Exception as ex:
        return f"Error: {type(ex).__name__}: {ex}"


if __name__ == "__main__":
    host = os.environ.get("MCP_EXTRACT_PST_HOST", "0.0.0.0")
    port = int(os.environ.get("MCP_EXTRACT_PST_PORT", "9003"))
    path = os.environ.get("MCP_EXTRACT_PST_PATH", "/mcp")
    log_level = os.environ.get("MCP_EXTRACT_PST_LOG_LEVEL", "debug")

    asyncio.run(
        mcp.run(
            transport="streamable-http",
            host=host,
            port=port,
            path=path,
            log_level=log_level,
        )
    )
