from aspose.email.clients.pop3 import Pop3Client
from aspose.email.clients import SecurityOptions

# put here your POP3 server credentials
USER = "your_email@gmail.com"
PASSWORD = "xxxx yyyy zzzz aaaa"

def run():
    with Pop3Client() as client:
        # Specify host, username, password, Port and SecurityOptions for your client
        client.host = "pop.gmail.com";
        client.username = USER
        client.password = PASSWORD
        client.port = 995;
        client.security_options = SecurityOptions.AUTO;
        client.timeout = 5000
        print("Connected to POP3 server.");

if __name__ == '__main__':
    run()
