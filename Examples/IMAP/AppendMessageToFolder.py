from aspose.email.clients.imap import ImapClient
from aspose.email import MailMessage

# put here your IMAP server credentials
USER = "your_email@gmail.com"
PASSWORD = "xxxx yyyy zzzz aaaa"

def run():
    msg = MailMessage("user@domain1.com", "user@domain2.com", "subject", "message")

    with ImapClient("imap.gmail.com", 993, USER, PASSWORD) as client:
        client.select_folder("Inbox")
        client.subscribe_folder(client.current_folder.name)
        client.append_message(client.current_folder.name, msg)

if __name__ == '__main__':
    run()
