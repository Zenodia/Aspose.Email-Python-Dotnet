from aspose.email.clients.imap import ImapClient
from aspose.email.clients.imap import ImapQueryBuilder
import datetime as dt

# put here your IMAP server credentials
USER = "your_email@gmail.com"
PASSWORD = "xxxx yyyy zzzz aaaa"

def run():

    with ImapClient("imap.gmail.com", 993, USER, PASSWORD) as client:
        client.select_folder("Inbox")
        builder = ImapQueryBuilder()
        builder.subject.contains("email")
        builder.internal_date.on(dt.datetime.now())
        query = builder.get_query()
        msgsColl = client.list_messages(query)
        print("Total Messages fulfilling search criterion: " + str(len(msgsColl)))

if __name__ == '__main__':
    run()
