import os
import shutil
from pathlib import Path
from aspose.email.storage.pst import *

def run():

    dataDir = "Data/"
    #ExStart: MoveItemsToOtherFolders

    # make copy of pst to modify content
    pst_file = os.path.join(dataDir, "Outlook.pst")
    pst_file_copy = os.path.join(dataDir, "Outlook_copy.pst")
    shutil.copy(pst_file, pst_file_copy)

    with PersonalStorage.from_file(pst_file_copy) as personalStorage:

        # Get the format of the file
        inbox = personalStorage.root_folder.get_sub_folder("Inbox")

        deleted = personalStorage.get_predefined_folder(StandardIpmFolder.DELETED_ITEMS)

        #subfolder = inbox.get_sub_folder("SubInbox")
        # Add new folder "Inbox"
        subfolder = inbox.add_sub_folder("Inbox")


        # Move folder and message to the Deleted Items
        personalStorage.move_item(subfolder, deleted)
        contents = inbox.get_contents()
        personalStorage.move_item(contents[0], deleted)
            
        # Move all inbox subfolders and subfolder contents to the Deleted Items
        inbox.move_subfolders(deleted)
        subfolder.move_contents(deleted)
        #ExEnd: MoveItemsToOtherFolders

    Path.unlink(pst_file_copy)
    
if __name__ == '__main__':
    run()
