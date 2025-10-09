import os
from aspose.email.storage.pst import *

def run():
    dataDir = "Data/"
    #ExStart: AddFilesToPST
        
    pst_file = os.path.join(dataDir, "AddFilesToPst_out.pst")

    try:
        os.remove(pst_file)
    except FileNotFoundError:
        pass
    
    personalStorage = PersonalStorage.create(pst_file, FileFormatVersion.UNICODE)

    folder = personalStorage.root_folder.add_sub_folder("Files")

    folder.add_file(dataDir + "FileToBeAddedToPST.txt", "")
    #ExEnd: AddFilesToPST

if __name__ == '__main__':
    run()
