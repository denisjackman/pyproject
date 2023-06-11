''' 
    this is swiss army knife for testing gcp 
    reference:
    https://ericmjl.github.io/blog/2023/3/8/how-to-automate-the-creation-of-google-docs-with-python/
'''
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

def main():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)
    # Create Google Docs file
    file = drive.CreateFile({'title': 'Hello Google Drive!'})
    file.Upload()
    print('Created file %s with mimeType %s' % (file['title'], file['mimeType']))
    
if __name__ == '__main__':
    main()