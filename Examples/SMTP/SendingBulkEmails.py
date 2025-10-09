import aspose.email as ae
from aspose.email.clients.smtp import SmtpClient
from aspose.email.clients import SecurityOptions
from aspose.email import MailMessage
from aspose.email import MailMessageCollection

# put here your SMTP server credentials
USER = "your_email@gmail.com"
PASSWORD = "xxxx yyyy zzzz aaaa"

def run():
    message1 = MailMessage("from@gmail.com", "to@gmail.com", "Sending Bulk Emails using Aspose.Email", "message1, how are you?")
    message2 = MailMessage("from@gmail.com", "to@gmail.com", "Sending Bulk Emails using Aspose.Email", "message2, how are you?")
    message3 = MailMessage("from@gmail.com", "to@gmail.com", "Sending Bulk Emails using Aspose.Email", "message3, how are you?")

    manyMsg =  MailMessageCollection()
    manyMsg.append(message1)
    manyMsg.append(message2)
    manyMsg.append(message3)

    #Send using Smtp Client
    with SmtpClient("smtp.gmail.com", 465, USER, PASSWORD) as client:
        client.security_options = SecurityOptions.AUTO
        client.send(manyMsg)

if __name__ == '__main__':
    run()
