'''
    this is swiss army knife for testing gcp
    reference:
    https://ericmjl.github.io/blog/2023/3/8/how-to-automate-the-creation-of-google-docs-with-python/
'''
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive


def main():
    ''' main function       '''
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)
    # Create Google Docs file
    file = drive.CreateFile({'title': 'Hello Google Drive!'})
    file.Upload()
    print(f"Created file {file['title']}")


if __name__ == '__main__':
    main()
