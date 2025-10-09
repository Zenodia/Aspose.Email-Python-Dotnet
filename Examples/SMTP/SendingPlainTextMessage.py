import aspose.email as ae
from aspose.email.clients.smtp import SmtpClient
from aspose.email.clients import SecurityOptions
from aspose.email import MailMessage

# put here your SMTP server credentials
USER = "your_email@gmail.com"
PASSWORD = "xxxx yyyy zzzz aaaa"

def run():
    eml = ae.MailMessage()
    eml.subject = "Message with Plain Text Body"
    eml.body = "This is plain text body."
    eml.from_address = ae.MailAddress("from@gmail.com")
    eml.to.append(ae.MailAddress("to@gmail.com", "Recipient 1"))

    # Send using Smtp Client
    with SmtpClient("smtp.gmail.com", 465, USER, PASSWORD) as client:
        client.security_options = SecurityOptions.AUTO
        client.send(eml)

if __name__ == '__main__':
    run()
