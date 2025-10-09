from aspose.email.clients import SecurityOptions
from aspose.email.clients.smtp import SmtpClient
from aspose.email.clients import SecurityOptions
from aspose.email import MailMessage
from aspose.email import MailAddress
from aspose.email import DeliveryNotificationOptions


# put here your SMTP server credentials
USER = "your_email@gmail.com"
PASSWORD = "xxxx yyyy zzzz aaaa"

def run():
    
    message = MailMessage()
    message.from_address = MailAddress("sender@sender.com")
    message.to.append(MailAddress("receiver@receiver.com", "Receiver"))
    message.subject = "Using MailMessage Features"
    message.html_body = "<html><body>This is the Html body</body></html>"
    message.delivery_notification_options = DeliveryNotificationOptions.ON_SUCCESS
    message.headers.add("Return-Receipt-To", "sender@sender.com")
    message.headers.add("Disposition-Notification-To", "sender@sender.com")

    # Create an instance of SmtpClient Class and specify your mailing Host server, Username, Password and Port No
    with SmtpClient("smtp.gmail.com", 465, USER, PASSWORD) as client:
        client.security_options = SecurityOptions.AUTO
        # Client.Send will send this message
        client.send(message)
        # Display ‘Message Sent’, only if message sent successfully
        print("Message sent")
    
if __name__ == '__main__':
    run()
