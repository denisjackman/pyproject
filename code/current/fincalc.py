'''
    finance calculator
'''


def main():  # pylint: disable=R0914
    """ This is the main routine for the program """
    print("Starting the sequence:")
    amount_in = 0
    amount_out = 0
    count = 0
    year17_amount = 0
    year18_amount = 0
    year19_amount = 0
    year20_amount = 0
    year21_amount = 0
    year22_amount = 0
    year17_out = 0
    year18_out = 0
    year19_out = 0
    year20_out = 0
    year21_out = 0
    year22_out = 0

    with open("Z:/Store/house-data/consolidated.csv",
              encoding='utf-8-sig') as finfile:
        for line in finfile:
            if line.startswith("Transaction Date"):
                continue
            data = line.split(',')
            print(" date: "
                  f"{data[0]}"
                  " desc: "
                  f"{data[4]}"
                  " amount-out: "
                  f"{data[5]}"
                  " amount-in: "
                  f"{data[6]}")
            count += 1
            datedata = data[0].split('/')

            if data[5].strip() == "":
                amount_in += float(data[6])
                if datedata[2] == '2017':
                    year17_amount += float(data[6])
                if datedata[2] == '2018':
                    year18_amount += float(data[6])
                if datedata[2] == '2019':
                    year19_amount += float(data[6])
                if datedata[2] == '2020':
                    year20_amount += float(data[6])
                if datedata[2] == '2021':
                    year21_amount += float(data[6])
                if datedata[2] == '2022':
                    year22_amount += float(data[6])
            else:
                amount_out += float(data[5])
                if datedata[2] == '2017':
                    year17_out += float(data[5])
                if datedata[2] == '2018':
                    year18_out += float(data[5])
                if datedata[2] == '2019':
                    year19_out += float(data[5])
                if datedata[2] == '2020':
                    year20_out += float(data[5])
                if datedata[2] == '2021':
                    year21_out += float(data[5])
                if datedata[2] == '2022':
                    year22_out += float(data[5])
    print('------------------IN----------------------')
    print(f' 2017 total : {year17_amount}')
    print(f' 2018 total : {year18_amount}')
    print(f' 2019 total : {year19_amount}')
    print(f' 2020 total : {year20_amount}')
    print(f' 2021 total : {year21_amount}')
    print(f' 2022 total : {year22_amount}')
    print('------------------IN----------------------')
    print(f' 2017 total : {year17_out}')
    print(f' 2018 total : {year18_out}')
    print(f' 2019 total : {year19_out}')
    print(f' 2020 total : {year20_out}')
    print(f' 2021 total : {year21_out}')
    print(f' 2022 total : {year22_out}')
    print('----------------------------------------')
    print(f'total amount in  : {amount_in}')
    print(f'total amount out : {amount_out}')
    print(f'total amount diff: {amount_in - amount_out}')
    print(f"total records   : {count}")
    print('----------------------------------------')
    print("finishing up and closing down:")


if __name__ == '__main__':
    main()
