from aspose.email.storage.pst import *
from aspose.email.mapi import MapiCalendar
from aspose.email.mapi import MapiRecipientType
from aspose.email.mapi import MapiRecipientCollection
from aspose.email.mapi import MapiRecipient

import datetime as dt
from datetime import timedelta

import os

def run():
    dataDir = "Data/"

    with PersonalStorage.from_file(dataDir + "Outlook.pst", False) as personalStorage:
        for folder in personalStorage.root_folder.get_sub_folders():
            for messageInfo in folder.enumerate_messages():
                folderInfo = personalStorage.get_parent_folder(messageInfo.entry_id)
                print(folderInfo.display_name)
    
if __name__ == '__main__':
    run()
