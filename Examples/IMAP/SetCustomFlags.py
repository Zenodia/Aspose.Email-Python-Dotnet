from aspose.email.clients.imap import ImapClient
from aspose.email.clients.imap import ImapMessageFlags
from aspose.email import MailMessage

# put here your IMAP server credentials
USER = "your_email@gmail.com"
PASSWORD = "xxxx yyyy zzzz aaaa"


def run():
    with ImapClient("imap.gmail.com", 993, USER, PASSWORD) as client:
        message = MailMessage("user@domain1.com", "user@domain2.com", "subject", "message");
        #Append the message to mailbox
        uid = client.append_message("Inbox", message);
        client.add_message_flags(uid, ImapMessageFlags.keyword("custom1"))

if __name__ == '__main__':
    run()
