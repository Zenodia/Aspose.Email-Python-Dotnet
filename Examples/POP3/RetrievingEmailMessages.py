from aspose.email.clients.pop3 import Pop3Client
from aspose.email.clients import SecurityOptions

# put here your POP3 server credentials
USER = "your_email@gmail.com"
PASSWORD = "xxxx yyyy zzzz aaaa"

def run():
    with Pop3Client("pop.gmail.com", 995, USER, PASSWORD) as client:
        client.security_options = SecurityOptions.AUTO
        client.timeout = 5000

        messageCount = client.get_message_count();

        print("Total messages: " + str(messageCount))
        for i in range(0,messageCount):
            # Retrieve message    
            message = client.fetch_message(i+1)
            print("From:" + str(message.from_address))
            print("Subject:" + message.subject)
            print(len(message.html_body));


if __name__ == '__main__':
    run()
