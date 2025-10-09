from aspose.email.clients.pop3 import Pop3Client
from aspose.email.clients import SecurityOptions

def run():

    client = Pop3Client("imap.gmail.com", 993, "username", "password")
    client.security_options = SecurityOptions.AUTO
    client.timeout = 5000

    # Delete all the message one by one
    messageCount = client.get_message_count()

    print("Total messages in inbox: " + str(messageCount))

    for i in range(1,messageCount):
        client.delete_message(i)

    client.commit_deletes()


if __name__ == '__main__':
    run()
