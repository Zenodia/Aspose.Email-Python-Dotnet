from aspose.email.clients.pop3 import Pop3Client
from aspose.email.clients import SecurityOptions

# put here your POP3 server credentials
USER = "your_email@gmail.com"
PASSWORD = "xxxx yyyy zzzz aaaa"

def run():
    with Pop3Client("pop.gmail.com", 995, USER, PASSWORD) as client:
        client.security_options = SecurityOptions.AUTO
        client.timeout = 5000

        #Get the size of the mailbox,  Get mailbox info, number of messages in the mailbox
        count = client.get_message_count();
        print("No. of emails: " + str(count));

if __name__ == '__main__':
    run()
