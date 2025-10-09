import os
import shutil 
from aspose.email.storage.pst import *

def run():
    dataDir = "Data/"
    #ExStart: DeleteMessagesFromPSTFile

    # make copy of pst for content modification
    pst_file = os.path.join(dataDir, "Outlook.pst")
    pst_file_copy = os.path.join(dataDir, "Outlook_copy.pst")
    shutil.copy(pst_file, pst_file_copy)

    with PersonalStorage.from_file(pst_file_copy) as pst:
            
        # Get the format of the file
        folder = pst.get_predefined_folder(StandardIpmFolder.SENT_ITEMS)

        print("Total messges count in folder: " + str(len(folder.get_contents())))

        #Delete First Item
        msgsColl = folder.get_contents()
        msgInfo = msgsColl[0]

        folder.delete_child_item(msgInfo.entry_id)

        print("Total messges count in folder after deletion: " + str(len(folder.get_contents())))
        #ExEnd: DeleteMessagesFromPSTFile

    os.unlink(pst_file_copy)
    
if __name__ == '__main__':
    run()
