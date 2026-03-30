---
name: pst-mailbox
description: >
  Query, search, browse, and draft emails in Outlook PST files via an MCP server.
  Use when the user asks about emails, mailbox contents, folder structure, searching
  by sender or subject, extracting emails, drafting replies, or any PST/Outlook-related
  task. Trigger keywords: email, mail, pst, outlook, inbox, draft, sender, mailbox,
  folder, unread.
---

# PST Mailbox Skill

Interact with Outlook `.pst` files through a running MCP server.

## Prerequisites

- MCP server running at `http://host.openshell.internal:9003/mcp`
- Python `fastmcp` package installed

## Available Tools

Call via: `python3 scripts/pst_client.py <tool_name> '<json_args>'`

All paths below are relative to this skill's directory.

| Tool | Purpose | Required args |
|---|---|---|
| `pst_agent` | Natural language query — LLM dispatches to the right tool | `{"query": "...", "pst_path": "..."}` |
| `extract_pst` | Extract all emails from PST | `{"pst_path": "..."}` |
| `search_emails_by_sender` | Find emails from a specific sender | `{"pst_path": "...", "sender": "..."}` |
| `get_latest_emails` | Get N most recent emails | `{"pst_path": "...", "count": N}` |
| `list_pst_folders` | Show folder tree with counts | `{"pst_path": "..."}` |
| `search_emails_by_subject` | Search emails by subject keyword | `{"pst_path": "...", "subject": "..."}` |
| `draft_email` | Draft an email (returns MSG/EML content) | `{"to": "...", "subject": "...", "body": "...", "pst_path": "..."}` |

## Workflow

### Choosing the right tool

- **User asks a vague or complex question** → use `pst_agent` (it picks the right sub-tool)
- **User asks something specific** (e.g., "emails from alice@...") → call the specific tool directly for speed

### Common patterns

**Browse mailbox structure:**
```bash
python3 scripts/pst_client.py list_pst_folders '{"pst_path": "/path/to/file.pst"}'
```

**Get recent emails:**
```bash
python3 scripts/pst_client.py get_latest_emails '{"pst_path": "/path/to/file.pst", "count": 10}'
```

**Search by sender:**
```bash
python3 scripts/pst_client.py search_emails_by_sender '{"pst_path": "/path/to/file.pst", "sender": "someone@example.com"}'
```

**Search by subject:**
```bash
python3 scripts/pst_client.py search_emails_by_subject '{"pst_path": "/path/to/file.pst", "subject": "project kickoff"}'
```

**Natural language query (delegates to the best tool):**
```bash
python3 scripts/pst_client.py pst_agent '{"query": "show me unread emails about invoices", "pst_path": "/path/to/file.pst"}'
```

**Draft an email:**
```bash
python3 scripts/pst_client.py draft_email '{"to": "bob@example.com", "subject": "Meeting follow-up", "body": "Hi Bob, ...", "pst_path": "/path/to/file.pst"}'
```

## Notes

- The PST path must be accessible from the MCP server host.
- `pst_agent` uses an LLM on the server side to route queries — it's convenient but slower than calling a specific tool directly.
- For large mailboxes, prefer targeted searches over `extract_pst` to avoid huge outputs.
- If the user hasn't specified a PST path, ask them for it (or check TOOLS.md for a default).
