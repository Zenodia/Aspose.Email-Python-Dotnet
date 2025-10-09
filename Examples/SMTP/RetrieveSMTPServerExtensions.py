from aspose.email.clients.smtp import SmtpClient
from aspose.email.clients import SecurityOptions

# put here your SMTP server credentials
USER = "your_email@gmail.com"
PASSWORD = "xxxx yyyy zzzz aaaa"

def run():
    with SmtpClient("smtp.gmail.com", 465, USER, PASSWORD) as client:
        client.security_options = SecurityOptions.AUTO
        for str in client.get_capabilities():
            print(str)

if __name__ == '__main__':
    run()
