'''
    file utilities
'''
import shutil


def move_file(source_path, destination_path):
    '''
        a function to move a file
    '''
    result = False
    try:
        shutil.move(source_path, destination_path)
        print(f'File {source_path} moved to {destination_path}')
        result = True
    except OSError as err:
        print(f'File {source_path} NOT moved to {destination_path} : {err}')
    return result


def main():
    """ This is the main routine for the program """
    print("Starting the sequence:")
    if move_file(r'file.txt', r'Z:/pyproject/scratch/output'):
        print('moved the file')
    else:
        print('did not move the file')
    if move_file(r'Z:/pyproject/scratch/output/file.txt', r'.'):
        print('moved the file')
    else:
        print('did not move the file')

    print("finishing up and closing down:")


if __name__ == '__main__':
    main()
