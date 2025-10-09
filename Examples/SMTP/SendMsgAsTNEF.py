import aspose.email as ae
from aspose.email.clients.smtp import SmtpClient
from aspose.email.clients import SecurityOptions
from aspose.email import MailMessage
from aspose.email import MailAddress

# put here your SMTP server credentials
USER = "your_email@gmail.com"
PASSWORD = "xxxx yyyy zzzz aaaa"

def run():
    dataDir = "Data/"

    eml = MailMessage.load(dataDir + "Message.eml")
    eml.subject = "Send message as TNEF"
    eml.from_address = MailAddress("from@gmail.com")
    eml.to.append(ae.MailAddress("to@gmail.com", "Recipient 1"))

    # Send using Smtp Client
    with SmtpClient("smtp.gmail.com", 465, USER, PASSWORD) as client:
        client.security_options = SecurityOptions.AUTO
        client.use_tnef= True
        client.send(eml)

if __name__ == '__main__':
    run()
