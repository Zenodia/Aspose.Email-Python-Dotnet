#!/usr/bin/env python3
"""
MCP client for extract_pst_mcp_server.py — thin wrapper to call tools over streamable HTTP.

Usage:
  python extract_pst_mcp_client.py extract_pst --pst C:\\path\\file.pst [--max-emails N] [--max-contacts N]
  python extract_pst_mcp_client.py draft_email --subject "Hi" --to "a@b.com" --out draft.msg
  python extract_pst_mcp_client.py draft_email --subject "Hi" --to "a@b.com" --append-to-pst C:\\path\\file.pst

Environment:
  MCP_EXTRACT_PST_SERVER_URL — default http://127.0.0.1:9001/mcp

Exit codes:
  0  success (report on stdout)
  1  error (message on stderr)
"""

from __future__ import annotations

import argparse
import asyncio
import json
import os
import sys
import warnings

os.environ.setdefault("PYTHONWARNINGS", "ignore::DeprecationWarning")
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", message=".*streamable_http_client.*")

MCP_SERVER_URL = os.environ.get(
    "MCP_EXTRACT_PST_SERVER_URL",
    "http://127.0.0.1:9001/mcp",
)

async def call_mcp(tool_name: str, arguments: dict, server_url: str) -> str:
    from fastmcp import Client

    async with Client(server_url) as client:
        result = await client.call_tool(tool_name, arguments)

    if hasattr(result, "content") and result.content:
        return result.content[0].text
    if isinstance(result, dict):
        return result.get("text", json.dumps(result))
    return str(result)


def _build_extract_args(ns: argparse.Namespace) -> dict:
    d: dict = {"pst_path": ns.pst}
    if ns.max_emails is not None:
        d["max_emails"] = ns.max_emails
    if ns.max_contacts is not None:
        d["max_contacts"] = ns.max_contacts
    return d


def _build_draft_args(ns: argparse.Namespace) -> dict:
    d: dict = {
        "subject": ns.subject or "",
        "body": ns.body or "",
        "to_addresses": ns.to_addresses or "",
        "cc_addresses": ns.cc_addresses or "",
        "bcc_addresses": ns.bcc_addresses or "",
        "file_format": ns.file_format,
    }
    if ns.from_address is not None:
        d["from_address"] = ns.from_address
    if ns.body_file is not None:
        d["body_file"] = ns.body_file
    if ns.out_path is not None:
        d["out_path"] = ns.out_path
    if ns.append_to_pst is not None:
        d["append_to_pst"] = ns.append_to_pst
    return d


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Call ExtractPst MCP tools (extract_pst, draft_email)."
    )
    parser.add_argument(
        "--url",
        default=MCP_SERVER_URL,
        help=f"MCP streamable HTTP endpoint (default: env MCP_EXTRACT_PST_SERVER_URL or {MCP_SERVER_URL})",
    )
    sub = parser.add_subparsers(dest="tool", required=True)

    p_ext = sub.add_parser("extract_pst", help="List contacts and emails from a PST")
    p_ext.add_argument("--pst", required=True, help="Path to .pst on the server host")
    p_ext.add_argument("--max-emails", type=int, default=None, metavar="N")
    p_ext.add_argument("--max-contacts", type=int, default=None, metavar="N")

    p_dr = sub.add_parser("draft_email", help="Create a draft MSG/EML and/or add to PST Drafts")
    p_dr.add_argument("--subject", default="")
    p_dr.add_argument("--body", default="")
    p_dr.add_argument("--to", dest="to_addresses", default="")
    p_dr.add_argument("--cc", dest="cc_addresses", default="")
    p_dr.add_argument("--bcc", dest="bcc_addresses", default="")
    p_dr.add_argument("--from", dest="from_address", default=None)
    p_dr.add_argument("--body-file", dest="body_file", default=None)
    p_dr.add_argument("--out", dest="out_path", default=None)
    p_dr.add_argument("--format", dest="file_format", choices=("msg", "eml"), default="msg")
    p_dr.add_argument("--append-to-pst", dest="append_to_pst", default=None)

    args = parser.parse_args()
    server_url = args.url

    if args.tool == "extract_pst":
        payload = _build_extract_args(args)
    else:
        payload = _build_draft_args(args)

    try:
        out = asyncio.run(call_mcp(args.tool, payload, server_url))
        print(out)
    except Exception as e:
        print(f"Error calling MCP server: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
