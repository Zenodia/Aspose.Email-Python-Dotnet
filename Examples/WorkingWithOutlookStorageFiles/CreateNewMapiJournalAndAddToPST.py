import os
from aspose.email.storage.pst import *
from aspose.email.mapi import MapiJournal

import datetime as dt
from datetime import timedelta

def run():
    dataDir = "Data/"
    #ExStart: CreateNewMapiJournalAndAddToPST
    journal =MapiJournal("daily record", "called out in the dark", "Phone call", "Phone call")
    journal.start_time = dt.datetime.now();
    journal.end_time = dt.datetime.today() + timedelta(hours=1)


    pst_file = os.path.join(dataDir, "CreateNewMapiJournalAndAddToPST_out.pst")

    try:
        os.remove(pst_file)
    except FileNotFoundError:
        pass

    personalStorage = PersonalStorage.create(pst_file, FileFormatVersion.UNICODE)

    tasksFolder = personalStorage.create_predefined_folder("Journal", StandardIpmFolder.JOURNAL)
    tasksFolder.add_mapi_message_item(journal)

    #ExEnd:CreateNewMapiJournalAndAddToPST
    
if __name__ == '__main__':
    run()
