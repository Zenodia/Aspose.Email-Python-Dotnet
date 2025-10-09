from aspose.email.clients.smtp import SmtpClient
from aspose.email.clients import SecurityOptions

# put here your SMTP server credentials
USER = "your_email@gmail.com"
PASSWORD = "xxxx yyyy zzzz aaaa"

def run():
    with SmtpClient() as client:
        client.host = "smtp.gmail.com"
        client.port = 465
        client.username = USER
        client.password = PASSWORD
        client.security_options = SecurityOptions.SSL_EXPLICIT

if __name__ == '__main__':
    run()
