from aspose.email.clients.imap import ImapClient
from aspose.email.clients import SecurityOptions

# put here your IMAP server credentials
USER = "your_email@gmail.com"
PASSWORD = "xxxx yyyy zzzz aaaa"


def run():

    with ImapClient("imap.gmail.com", 993, USER, PASSWORD) as client:   
        folderInfoColl = client.list_folders()

        #Iterate through the collection to get folder info one by one
        for folderInfo in folderInfoColl:
            print(f"Folder name is '{folderInfo.name}'")
            folderExtInfo = client.get_folder_info(folderInfo.name)
            if folderExtInfo:
                print("  New message count: " + str(folderExtInfo.new_message_count))
                print("  Is it readonly? " + str(folderExtInfo.read_only))
                print("  Total number of messages " + str(folderExtInfo.total_message_count))


if __name__ == '__main__':
    run()
