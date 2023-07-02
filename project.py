''' This is a sample project to resuse utilities and stuff '''
from djcode.current.fileutility import walk_through
from djcode.current.fileutility import extract_file_extension
from djcode.current.myfunctions.utensils import dish
from tqdm import tqdm

START_DIRECTORY ='Y:\\'

def main():
    ''' this is the main utility '''
    print('[+] Starting project file running ')
    print(f'[-] Dish is {dish()}')
    totallist = []
    commands = {"verbosemode":False, "deletemode":False, "startdirectory":START_DIRECTORY}
    totallist.extend(walk_through(commands))
    print(f"[-] Records found {len(totallist):,}")
    pdflist = []
    for item in tqdm(totallist, total=len(totallist), unit=' item'):
        tmpext = extract_file_extension(item)
        if tmpext == '.pdf':
            if 'site-packages' not in item:
                pdflist.extend(item)
    print(f'[-] Total PDF files is {len(pdflist):,}')
    print('[+] Finished ')

if __name__ == '__main__':
    main()
