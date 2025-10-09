import os
from aspose.email.clients.imap import ImapClient
from aspose.email.clients import SecurityOptions

# put here your IMAP server credentials
USER = "your_email@gmail.com"
PASSWORD = "xxxx yyyy zzzz aaaa"


def run():
    dataDir = "out"
    os.makedirs(dataDir, exist_ok=True)

    with ImapClient("imap.gmail.com", 993, USER, PASSWORD) as conn:
        conn.security_options = SecurityOptions.AUTO

        conn.select_folder("Inbox")
        
        messages = conn.list_messages()
        messages_count = len(messages)
        print(f"Total nubler of messages: {messages_count}")
        count = 0
        for msg in messages:
            out_file = os.path.join(dataDir, msg.unique_id + "_out.eml")
            conn.save_message(msg.unique_id, out_file)
            print(f'\rWrote {count} of {messages_count}', end='')
            count += 1

        print(f"\n{messages_count} messages written to '{dataDir}'")


if __name__ == '__main__':
    run()
