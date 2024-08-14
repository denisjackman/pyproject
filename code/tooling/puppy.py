''' this is the puppy utility '''
import os
import shutil
import datetime
import zipfile36 as zipfile
import exifread
from tqdm import tqdm
# variables
ZIPFILE = 'T://pictures.zip'
TARGETDIR = 'S:'
TARDIR = 'S://pictures'


def get_exif_data(ged_filename):
    ''' get exif data '''
    with open(ged_filename,
              'rb') as ged_file:
        ged_tags = exifread.process_file(ged_file, details=False)
    return ged_tags


def main():
    ''' main '''
    print('[*] puppy main starting up')
    print(f'[-] extracting {ZIPFILE} to {TARGETDIR}')
    filedate = datetime.datetime.now()
    filedatestr = f'T:puppy_{filedate.year}{filedate.month}{filedate.day}.txt'
    try:
        with zipfile.ZipFile(ZIPFILE) as archive:
            archive.extractall(path=TARGETDIR)
    except:  # pylint: disable=bare-except
        print('[o] error extracting zipfile')
    file_count = 0
    print('[-] opening target file '
          )
    with open(filedatestr, 'w', encoding='utf-8-sig') as puppy_file:
        print('[-] puppy main walking through files')
        for root, _, files in os.walk(TARDIR):
            for item_file in tqdm(files, total=len(files), unit=' item_file'):
                file_count += 1
                # Calculate the hash of the file.
                file_path = os.path.join(root, item_file)
                exif_data = get_exif_data(file_path)
                puppy_file.write(f'{file_path},{exif_data}')
    print(f'[-] {file_count} files found')
    print(f'[-] removing moving {TARDIR}')
    shutil.rmtree(TARDIR)
    print(f'[-] {TARDIR} removed')
    print('[*] puppy main shutting down')


if __name__ == "__main__":
    print('[+] puppy starting up')
    main()
    print('[+] puppy shutting down')
