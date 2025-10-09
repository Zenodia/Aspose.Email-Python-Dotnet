from aspose.email.storage.pst import *
from aspose.email.mapi import MapiMessage

def run():
	dataDir = "Data/"
	#ExStart: ChangeFolderContainerClass
	pst = PersonalStorage.from_file(dataDir + "PstWithPython_out.pst")

	folder = pst.root_folder.get_sub_folder("Inbox")

	folder.change_container_class("IPF.Note")

	#ExEnd: ChangeFolderContainerClass
	
if __name__ == '__main__':
    run()
