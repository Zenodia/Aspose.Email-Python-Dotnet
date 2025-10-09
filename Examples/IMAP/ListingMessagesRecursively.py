from aspose.email.clients.imap import ImapClient

# put here your IMAP server credentials
USER = "your_email@gmail.com"
PASSWORD = "xxxx yyyy zzzz aaaa"

def run():
    with ImapClient("imap.gmail.com", 993, USER, PASSWORD) as conn:
        conn.select_folder("Inbox")
        msgsColl = conn.list_messages(True);
        print("Total Messages: " + str(len(msgsColl)))

if __name__ == '__main__':
    run()
