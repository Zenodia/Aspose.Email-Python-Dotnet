from aspose.email.clients.imap import ImapClient
from aspose.email.clients.imap import PageSettings


# put here your IMAP server credentials
USER = "your_email@gmail.com"
PASSWORD = "xxxx yyyy zzzz aaaa"

def run():
    with ImapClient("imap.gmail.com", 993, USER, PASSWORD) as client:
        client.select_folder("Inbox")
        itemsPerPage = 10

        pageInfo = client.list_messages_by_page(itemsPerPage, 0, PageSettings())
        while not pageInfo.last_page:
            for info in pageInfo.items:
                print( f"From: {info.from_address}, Subject: '{info.subject}'")
            # retrieve next page
            pageInfo = client.list_messages_by_page(pageInfo.next_page, PageSettings())


if __name__ == '__main__':
    run()
