import os
import shutil
from aspose.email.storage.pst import *

def run():
    dataDir = "Data/"
    #ExStart: DeleteBulkItemsFromPst
        
    # make copy of pst to modify content
    pst_file = os.path.join(dataDir, "Outlook.pst")
    pst_file_copy = os.path.join(dataDir, "Outlook_copy.pst")
    shutil.copy(pst_file, pst_file_copy)

    with PersonalStorage.from_file(pst_file_copy) as pst:
                    
        # Get the format of the file
        folder = pst.get_predefined_folder(StandardIpmFolder.INBOX)

        print("Total messges count in folder: " + str(len(folder.get_contents())))

        # Create instance of PersonalStorageQueryBuilder
        queryBuilder = PersonalStorageQueryBuilder()

        queryBuilder.subject.contains("Microsoft")
        messages = folder.get_contents(queryBuilder.get_query());

        print("No. of Messages as per specified criterion: " + str(len(messages)))
        deleteList = []

        for messageInfo in messages:
                    deleteList.append(messageInfo.entry_id_string)

        folder.delete_child_items(deleteList)
        #ExEnd: DeleteBulkItemsFromPst

    os.unlink(pst_file_copy)
    
if __name__ == '__main__':
        run()
