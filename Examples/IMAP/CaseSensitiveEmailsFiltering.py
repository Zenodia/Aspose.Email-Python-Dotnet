from aspose.email.clients.imap import ImapClient
from aspose.email.clients.imap import ImapQueryBuilder

# put here your IMAP server credentials
USER = "your_email@gmail.com"
PASSWORD = "xxxx yyyy zzzz aaaa"

def run():
    try:
        with ImapClient("imap.gmail.com", 993, USER, PASSWORD) as client:
            client.select_folder("Inbox")
            builder = ImapQueryBuilder()
            builder.subject.contains("Newsletter", True)
                    
            query = builder.get_query()
            msgsColl = client.list_messages(query)
            print("Total Messages fulfilling search criterion: " + str(len(msgsColl)))

            for info in msgsColl:
                print(f"Message subject: {info.subject}");

    except Exception as ex:
        print(str(ex))

if __name__ == '__main__':
    run()
