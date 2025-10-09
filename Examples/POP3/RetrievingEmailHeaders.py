from aspose.email.clients.pop3 import Pop3Client
from aspose.email.clients import SecurityOptions

# put here your POP3 server credentials
USER = "your_email@gmail.com"
PASSWORD = "xxxx yyyy zzzz aaaa"

def run():
    with Pop3Client("pop.gmail.com", 995, USER, PASSWORD) as client:
        client.security_options = SecurityOptions.AUTO    
        client.timeout = 5000


        headers = client.get_message_headers(1)
        for index, header in enumerate(headers):
            print(header + " - ", end=" ")
            print (headers.get(index))

if __name__ == '__main__':
    run()
