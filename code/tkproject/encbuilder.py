''' encounter builder'''
import csv

ENC_FILE = "Z:/Maturam/encbuilder.csv"


def enc_read_csv_file(ercf_filename):
    ''' read csv file '''
    ercf_result = []
    with open(ercf_filename,
              'r',
              encoding='utf-8-sig') as ercf_csvfile:
        ercf_data = csv.reader(ercf_csvfile, delimiter=',')
        for row in ercf_data:
            ercf_result.append(row)
    return ercf_result


def main():
    ''' encounter builder'''
    print("[Encounter Builder] Starting...")
    enc_data = enc_read_csv_file(ENC_FILE)

    print("[Encounter Builder] Generating an encounter")
    main_input = input("[-] Party Level: ")
    if not main_input.isnumeric():
        print("[+] Please enter a number")
    else:
        main_party_size = input("[-] Party Size: ")
        if not main_party_size.isnumeric():
            print("[+] Please enter a number")
        else:
            print(f'[-] {enc_data[0]}')
            print(f'[-] {enc_data[int(main_input)][0]}'
                  f' {enc_data[int(main_input)][1]}'
                  f' {enc_data[int(main_input)][int(main_party_size)-1]}')
    # print("[Encounter Builder] Generating a monster...")
    # print("[Encounter Builder] Generating a trap...")
    # print("[Encounter Builder] Generating a treasure...")
    # print("[Encounter Builder] Generating a name...")
    print("[Encounter Builder] Complete")


if __name__ == "__main__":
    main()
