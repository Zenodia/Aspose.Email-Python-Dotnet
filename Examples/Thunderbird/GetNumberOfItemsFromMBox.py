from aspose.email.storage.mbox import MboxrdStorageReader
from aspose.email.storage.mbox import MboxLoadOptions

def run():
    dataDir = "Data/"
    with MboxrdStorageReader(dataDir + "ExampleMbox.mbox", MboxLoadOptions()) as reader:
        print("Total items in MBox file: " + str(reader.get_total_items_count()))

if __name__ == '__main__':
    run()
