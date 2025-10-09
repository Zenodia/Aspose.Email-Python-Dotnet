import os
from aspose.email.storage.pst import *
from aspose.email.mapi import MapiMessage

def run():
    dataDir = "Data/"
    #ExStart: CreateNewPSTFileAndAddingSubfolders

    pst_file = os.path.join(dataDir, "PstWithPython_out.pst")

    try:
        os.remove(pst_file)
    except FileNotFoundError:
        pass

    pst = PersonalStorage.create(pst_file, FileFormatVersion.UNICODE)

    # Add new folder "Inbox"
    pst.root_folder.add_sub_folder("Inbox");

    #ExEnd: CreateNewPSTFileAndAddingSubfolders
    
if __name__ == '__main__':
    run()
