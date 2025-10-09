import os
from pathlib import Path
from aspose.email.storage.pst import *
from aspose.email.mapi import MapiMessage

def run():
    dataDir = "Data/"
    #ExStart: AddMessagesFromOtherPST
    sourcePst = PersonalStorage.from_file(dataDir + "Outlook.pst", False)

    # Add new folder "Inbox"
    sourceFolder = sourcePst.root_folder.get_sub_folder("Inbox")

    pst_file = os.path.join(dataDir, "DestinationPst_out.pst")    
    Path.unlink(pst_file, missing_ok=True)

    with PersonalStorage.create(pst_file, FileFormatVersion.UNICODE) as destPst:

        # Add new folder "Inbox"
        destFolder = destPst.root_folder.add_sub_folder("Inbox")

        sourceMsgs = sourceFolder.get_contents()

        destFolder.add_messages(sourceFolder.enumerate_mapi_messages())

        #Verify that the messages have been added to the destination PST
        print(str(destFolder.content_count))
        #ExEnd: AddMessagesFromOtherPST

    Path.unlink(pst_file)
    
if __name__ == '__main__':
    run()
