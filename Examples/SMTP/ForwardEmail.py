import aspose.email as ae
from aspose.email.clients.smtp import SmtpClient
from aspose.email.clients import SecurityOptions
from aspose.email import MailMessage, MailAddress

# put here your SMTP server credentials
USER = "your_email@gmail.com"
PASSWORD = "xxxx yyyy zzzz aaaa"

def run():
    dataDir = "Data/"
    eml = MailMessage.load(dataDir + "Message.eml")
    eml.from_address = MailAddress("kashif.iqbal.aspose@gmail.com")

    # Send using Smtp Client
    with SmtpClient("smtp.gmail.com", 465, USER, PASSWORD) as client:
        client.security_options = SecurityOptions.AUTO
        client.forward("Recipient1@domain.com", "Recipient2@domain.com", eml)

if __name__ == '__main__':
    run()
