from aspose.email.clients.imap import ImapClient
from aspose.email.clients import SecurityOptions

# put here your IMAP server credentials
USER = "your_email@gmail.com"
PASSWORD = "xxxx yyyy zzzz aaaa"

def run():
    with ImapClient("imap.gmail.com", 993, USER, PASSWORD) as client:
        capabilities = client.get_capabilities()
        for val in capabilities:
            print(val);

if __name__ == '__main__':
    run()
