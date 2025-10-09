import os
from aspose.email.storage.pst import *
from aspose.email.mapi import MapiMessage

def run():
    dataDir = "Data/"
    #ExStart: AddMessagesToPSTFiles
      
    pst_file = os.path.join(dataDir, "AddMessagesToPst_out.pst")

    try:
        os.remove(pst_file)
    except FileNotFoundError:
        pass

    pst = PersonalStorage.create(pst_file, FileFormatVersion.UNICODE)

    # Add new folder "Inbox"
    inboxFolder = pst.root_folder.add_sub_folder("Inbox");

    # Add message to Inbox Folder
    inboxFolder.add_message(MapiMessage.load(dataDir + "MapiMsgWithPoll.msg"))

    #ExEnd: AddMessagesToPSTFiles
    
if __name__ == '__main__':
    run()
