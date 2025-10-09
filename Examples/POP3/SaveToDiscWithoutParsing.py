from aspose.email.clients.pop3 import Pop3Client
from aspose.email.clients import SecurityOptions

# put here your POP3 server credentials
USER = "your_email@gmail.com"
PASSWORD = "xxxx yyyy zzzz aaaa"

def run():
    dataDir = "Data/"
    with Pop3Client("pop.gmail.com", 995, USER, PASSWORD) as client:
        client.security_options = SecurityOptions.AUTO
        client.timeout = 5000

        try:
            # Save message to disk by message sequence number
            client.save_message(1, dataDir + "SaveToDiscWithoutParsing_out.eml")

        except Exception as ex:
            print(str(ex))

if __name__ == '__main__':
    run()
