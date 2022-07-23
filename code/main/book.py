import urllib.request
import json

isbn = '9780007550258'
name = "I%20Robot"
name = "V%20for%20Vendetta"

while True:

    base_api_link = "https://www.googleapis.com/books/v1/volumes?q=isbn:"
    # title search
    base_api_link = "https://www.googleapis.com/books/v1/volumes?q="
    # user_input = input("Enter ISBN: ").strip()
    # user_input = isbn
    user_input = name
    # this is a test

    with urllib.request.urlopen(base_api_link + user_input) as f:
        text = f.read()

    decoded_text = text.decode("utf-8")
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
