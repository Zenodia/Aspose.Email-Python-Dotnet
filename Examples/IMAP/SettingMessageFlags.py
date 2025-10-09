from aspose.email.clients.imap import ImapClient
from aspose.email.clients.imap import ImapMessageFlags

# put here your IMAP server credentials
USER = "your_email@gmail.com"
PASSWORD = "xxxx yyyy zzzz aaaa"

def run():

    with ImapClient("imap.gmail.com", 993, USER, PASSWORD) as conn:
        conn.select_folder("Inbox")
        conn.change_message_flags(1, ImapMessageFlags.is_read)

        conn.remove_message_flags(1, ImapMessageFlags.is_read)

if __name__ == '__main__':
    run()
