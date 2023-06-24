'''
    example book api call
'''
import urllib.request
import json

ISBN = '9780007550258'
NAME = "I%20Robot"
NAME = "V%20for%20Vendetta"

while True:

    BASE_API_LINK = "https://www.googleapis.com/books/v1/volumes?q=ISBN:"
    # title search
    BASE_API_LINK = "https://www.googleapis.com/books/v1/volumes?q="
    # USER_INPUT = input("Enter ISBN: ").strip()
    # USER_INPUT = ISBN
    USER_INPUT = NAME
    # this is a test

    with urllib.request.urlopen(BASE_API_LINK + USER_INPUT) as f:
        text = f.read()

    decoded_text = text.decode('utf-8-sig')
    obj = json.loads(decoded_text)
    # deserializes decoded_text to a Python object
    volume_info = obj["items"][0]
    authors = obj["items"][0]["volumeInfo"]["authors"]

    # displays title, summary, author, domain, page count and language
    print("\nTitle:", volume_info["volumeInfo"]["title"])
    print("\n")
    # print("\nISBN: ", volume_info["volumeInfo"]["industryIdentifiers"]
    #                    ["ISBN_13"])
    # print("\nSummary:\n")
    # print(textwrap.fill(volume_info["searchInfo"]["textSnippet"], width=65))
    print("\nAuthor(s):", ",".join(authors))
    # print("\nPublic Domain:", volume_info["accessInfo"]["publicDomain"])
    # print("\nPage count:", volume_info["volumeInfo"]["pageCount"])
    # print("\nLanguage:", volume_info["volumeInfo"]["language"])
    print("\n***")

    status_update = input("\nEnter another ISBN? y or n: ").lower().strip()

    if status_update == "n":
        print("\nThank you! Have a nice day.")
        break
