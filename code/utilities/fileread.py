'''
    file operations
'''
path = input("Enter the file path to read:")
with open(path, "r", encoding='utf8') as file:
    print(file.read())
input('Press Enter...')
