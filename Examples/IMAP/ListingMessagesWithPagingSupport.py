import aspose.email
from aspose.email.clients.imap import ImapClient
from aspose.email.clients.imap import PageSettings
from aspose.email.clients import SecurityOptions

# put here your IMAP server credentials
USER = "your_email@gmail.com"
PASSWORD = "xxxx yyyy zzzz aaaa"

def run():

    client = ImapClient("imap.gmail.com", 993, USER, PASSWORD)
    client.select_folder("Inbox")

    itemsPerPage = 10
    pageInfo = client.list_messages_by_page(itemsPerPage, 0, PageSettings())
    print(f'Total message count: {pageInfo.total_count}')

    while not pageInfo.last_page:
        # output messages subject from the current page
        print(f'Messages #{pageInfo.page_offset} - #{pageInfo.page_offset + itemsPerPage}:')
        for info in pageInfo.items:
            print(f'{info.unique_id}:{info.subject}')
        # retrieve next page
        pageInfo = client.list_messages_by_page(pageInfo.next_page, PageSettings())

if __name__ == '__main__':
    run()
