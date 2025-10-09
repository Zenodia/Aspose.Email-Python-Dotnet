import aspose.email
from aspose.email.clients.imap import ImapClient
from aspose.email.clients import SecurityOptions
from aspose.email import MailMessage

# put here your IMAP server credentials
USER = "your_email@gmail.com"
PASSWORD = "xxxx yyyy zzzz aaaa"

def run():
    
    dataDir = ""

    #ExStart: MoveMessageToAnotherFolder
    client = ImapClient("imap.gmail.com", 993, USER, PASSWORD)
    client.select_folder("Inbox")
    folderName = "N1Renamed"

    try:
        client.create_folder(folderName)
    except:
        pass

    #Append a new Message to Inbox
    msg = MailMessage("user@domain1.com", "user@domain2.com", "subject", "message")
    msgId = client.append_message( msg)
    
    #List messages from Inbox
    msgsCollection = client.list_messages()
    print("Total Messages in Inbox: " + str(len(msgsCollection)))

    #Move message to another folder
    client.move_message(msgId, folderName)

    #List messages from Inbox
    msgsCollection = client.list_messages()
    print("Total Messages in Inbox: " + str(len(msgsCollection)))
    #ExEnd: MoveMessageToAnotherFolder    

if __name__ == '__main__':
    run()
