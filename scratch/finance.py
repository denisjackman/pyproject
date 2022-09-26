'''
    custom finance tool for Jackman family
'''

def main():
    """ This is the main routine for the program """
    file1 = "Y:/house-data/joint-2016.csv"
    file2 = "Y:/house-data/joint-2017.csv"
    file3 = "Y:/house-data/joint-2018.csv"
    file4 = "Y:/house-data/joint-2019.csv"
    file5 = "Y:/house-data/joint-2020.csv"
    file6 = "Y:/house-data/joint-2021.csv"
    file7 = "Y:/house-data/joint-2022.csv"
    file8 = "Y:/house-data/joint-2022-late.csv"
    consolidated_file = "Y:/house-data/consolidated.csv"

    with open(consolidated_file, 'w', encoding='utf8') as outfile:
        for fname in [file1, file2, file3, file4, file5, file6, file7]:
            with open(fname, encoding='utf8') as infile:
                for line in infile:
                    outfile.write(line)

if __name__ == '__main__':
    main()
