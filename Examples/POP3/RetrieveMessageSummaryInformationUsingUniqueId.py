from aspose.email.clients.pop3 import Pop3Client
from aspose.email.clients import SecurityOptions

# put here your POP3 server credentials
USER = "your_email@gmail.com"
PASSWORD = "xxxx yyyy zzzz aaaa"

def run():
    with Pop3Client("pop.gmail.com", 995, USER, PASSWORD) as client:
        client.security_options = SecurityOptions.AUTO
        client.timeout = 5000

        uniqueId = "unique id of a message from server"

        messageInfo = None
        try:
            messageInfo = client.get_message_info(uniqueId)
        except:
            print('no such identifier')

        if messageInfo is not None:
            print(messageInfo.subject)
            print(messageInfo.date)

if __name__ == '__main__':
    run()
