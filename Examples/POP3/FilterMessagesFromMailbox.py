from aspose.email.clients.pop3 import Pop3Client
from aspose.email.clients import SecurityOptions
from aspose.email.tools.search import MailQueryBuilder 
import datetime as dt
from datetime import timedelta

# put here your POP3 server credentials
USER = "your_email@gmail.com"
PASSWORD = "xxxx yyyy zzzz aaaa"

def run():
    with Pop3Client("pop.gmail.com", 995, USER, PASSWORD) as client:
        client.security_options = SecurityOptions.AUTO
    
        builder = MailQueryBuilder()

        #Filtering on Subject
        builder.subject.contains("Newsletter")

        #Filtering on Internal Date
        builder.internal_date.on(dt.datetime.now())

        #Filtering on Date Range
        builder.internal_date.before(dt.datetime.now())
        builder.internal_date.since(dt.datetime.today() - timedelta(days=7))

        #Filtering on Sender
        builder.from_address.contains("saqib.razzaq@127.0.0.1")

        #Filtering on Specific Domain
        builder.from_address.contains("SpecificHost.com");
        
        #Filtering on specific Recipient
        builder.to.contains("recipient")

        #Case-Sensitive Email Filtering
        builder.subject.contains("Newsletter", True)

        msgsColl = client.list_messages(builder.get_query())

        print("Filtered Messages Count: " + str(len(msgsColl)))

if __name__ == '__main__':
    run()
