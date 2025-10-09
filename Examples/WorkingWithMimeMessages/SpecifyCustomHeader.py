import aspose.email as ae

# put here your SMTP server credentials
USER = "your_email@gmail.com"
PASSWORD = "xxxx yyyy zzzz aaaa"

def run():

    # Create an instance of MailMessage class
    eml = ae.MailMessage()
    
    # Specify ReplyTo, From, To field, Cc and Bcc Addresses
    eml.reply_to_list.append(ae.MailAddress("reply@reply.com"))
    eml.from_address = ae.MailAddress("sender@sender.com")
    eml.to.append(ae.MailAddress("to1@domain.com", "Recipient 1"))
    eml.subject = "test mail"
    eml.headers.add("secret-header", "mystery")
    
    with ae.clients.smtp.SmtpClient("smtp.gmail.com", 465, USER, PASSWORD) as client:
        # Client.Send will send this message
        client.send(eml)
        # Display ‘Message Sent’, only if message sent successfully
        print("Message sent")


if __name__ == '__main__':
    run()

