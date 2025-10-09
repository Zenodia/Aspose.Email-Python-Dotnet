from aspose.email.clients.imap import ImapClient
from aspose.email import MailMessage

USER = "your_email@gmail.com"
PASSWORD = "xxxx yyyy zzzz aaaa"

def run():

    with ImapClient("imap.gmail.com", 993, USER, PASSWORD) as client:
        client.select_folder("Inbox")
        message = MailMessage("from@Aspose.com", "to@Aspose.com", "Message deletion using IMAP Client", "EMAILNET-35227 Add ability in ImapClient to delete message")

        messageInfoCol = client.list_messages()
        print("Total messages in Inbox before appending: " + str(len(messageInfoCol)))

        emailId = client.append_message(message)
        print("Email appended to inbox with email Id: " + emailId)

        # Now verify that all the messages have been appended to the mailbox
        messageInfoCol = client.list_messages()
        print("Total messages in Inbox after appending: " + str(len(messageInfoCol)))

        client.delete_message(emailId)
        client.commit_deletes()
        messageInfoCol = client.list_messages()
        print("Total messages in Inbox after deletion: " + str(len(messageInfoCol)))


if __name__ == '__main__':
    run()
