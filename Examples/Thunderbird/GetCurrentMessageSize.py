from aspose.email.storage.mbox import MboxrdStorageReader
from aspose.email.storage.mbox import MboxLoadOptions

def run():
	dataDir = "Data/"
       
	with MboxrdStorageReader(dataDir + "ExampleMbox.mbox", MboxLoadOptions()) as reader:
		print(reader.current_data_size)
		eml = reader.read_next_message()

		# Read all messages in a loop
		while (eml is not None):
			print("Subject: " + eml.subject)
			eml = reader.read_next_message()

if __name__ == '__main__':
    run()
