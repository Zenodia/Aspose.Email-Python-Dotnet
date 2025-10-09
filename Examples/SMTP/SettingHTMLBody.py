import aspose.email as ae
from aspose.email.clients.smtp import SmtpClient
from aspose.email.clients import SecurityOptions
from aspose.email import MailMessage

# put here your SMTP server credentials
USER = "your_email@gmail.com"
PASSWORD = "xxxx yyyy zzzz aaaa"

def run():
    eml = ae.MailMessage()
    eml.subject = "Message with Html Body"
    eml.is_body_html = True
    eml.html_body = "<html><body>This is the <b>HTML</b>body</body></html>"
    eml.from_address = ae.MailAddress("from@gmail.com")
    eml.to.append(ae.MailAddress("to@gmail.com", "Recipient 1"))

    # Send using Smtp Client
    with SmtpClient("smtp.gmail.com", 465, USER, PASSWORD) as client:
        client.security_options = SecurityOptions.AUTO
        client.send(eml)

if __name__ == '__main__':
    run()
