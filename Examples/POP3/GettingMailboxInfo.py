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
        nSize = client.get_mailbox_size();
        print("Mailbox size is " + str(nSize) + " bytes.");
        info = client.get_mailbox_info();
        nMessageCount = info.message_count;
        print("Number of messages in mailbox are " + str(nMessageCount));
        nOccupiedSize = info.occupied_size;
        print("Occupied size is " + str(nOccupiedSize));

if __name__ == '__main__':
    run()
