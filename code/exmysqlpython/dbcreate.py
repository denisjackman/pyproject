'''DB create script  '''


def main():
    ''' main function '''
    print("[-] Starting Main")
    linecount = 0
    with open('Z:/Store/mysqlsampledatabase.sql',
              'r',
              encoding='utf-8-sig') as main_sql_file:
        for line in main_sql_file:
            if line != '\n':
                if not line.startswith('--'):
                    if not line.startswith('/*'):
                        if not line.startswith('CREATE DATABASE'):
                            print(line.strip())
                            linecount += 1
    print(f"[-] Line count {linecount}")
    print("[-] Main Complete")


if __name__ == '__main__':
    print("[+] Starting MySQL Database Build")
    main()
    print("[+] MySQL Database build complete")
