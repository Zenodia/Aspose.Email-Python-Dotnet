from aspose.email.clients.imap import ImapClient
from aspose.email.clients import SecurityOptions

def run():
    with ImapClient("imap.domain.com", 993, "user@domain.com", "pwd") as client:
        client.security_options = SecurityOptions.SSL_IMPLICIT

if __name__ == '__main__':
    run()
