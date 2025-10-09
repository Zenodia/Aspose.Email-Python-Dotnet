import os
import aspose.email
from aspose.email.clients.imap import ImapClient

# put here your IMAP server credentials
USER = "your_email@gmail.com"
PASSWORD = "xxxx yyyy zzzz aaaa"


def run():
    dataDir = "out"
    os.makedirs(dataDir, exist_ok=True)

    with ImapClient("imap.gmail.com", 993, USER, PASSWORD) as conn:
        conn.select_folder("Inbox")

        for msgInfo in conn.list_messages():
            msg = conn.fetch_message(msgInfo.unique_id)
            print(f'{msg.subject}')
            out_file = os.path.join(dataDir, msgInfo.unique_id + "_out.eml")
            msg.save(out_file, aspose.email.SaveOptions.default_msg_unicode)

if __name__ == '__main__':
    run()
