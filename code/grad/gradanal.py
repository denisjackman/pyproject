'''
    grad analysis script
'''
import csv

DATA_FILE = "Z:/Resources/development/GN-2016-sample-data.csv"


def opengradfile(csvfilename):
    ''' open csv file and send it back as a list '''
    csvlist = []
    result = []
    print("[+] --- Start Open CSV File ")
    with open(csvfilename, 'r', encoding='utf-8-sig') as csvfile:
        csvlist = csv.DictReader(csvfile, delimiter=",")
        for row in csvlist:
            result.append(row)
    print("[+] --- Finish Open CSV File ")
    return result


def gethorses(horselist):
    ''' return the dict of horse '''
    result = {}
    # for horse in horselist:
    print("[+] --- Start Get Horse")
    for item in horselist:
        if item["horse"] not in result:
            hpotreturn = float(item["odds"])*float(item["stake"])
            result[item["horse"]] = [item["horse"],
                                     item["result"],
                                     float(item["stake"]),
                                     float(item["return"]),
                                     hpotreturn,
                                     float(item["freebet_amount"]), 1]
        else:
            hstake = result[item["horse"]][2] + float(item["stake"])
            hreturn = result[item["horse"]][3] + float(item["return"])
            hpotreturn = result[item["horse"]][4] + float(item["odds"])*float(item["stake"])
            hfreebet = result[item["horse"]][5] + float(item["freebet_amount"])
            hcount = result[item["horse"]][6] + 1
            result[item["horse"]] = [item["horse"],
                                     item["result"],
                                     hstake,
                                     hreturn,
                                     hpotreturn,
                                     hfreebet,
                                     hcount]
    print("[+] --- Finish Get Horse")
    return result


def main():
    ''' main function '''
    print("[+] -- Main Function Start")
    dataset = opengradfile(DATA_FILE)
    print(f"[+] Number of items in dataset is {len(dataset)}")

    count = 0
    mdetails = {}
    ddetails = {}

    mdetails["mcount"] = 0
    mdetails["mstake"] = 0.0
    mdetails["mrev_cust"] = 0.0
    mdetails["mpot_cust"] = 0.0
    mdetails["mvoid"] = 0.0
    mdetails["mvoidcount"] = 0
    mdetails["mwin"] = 0
    mdetails["mplace"] = 0
    mdetails["mlose"] = 0

    ddetails["dcount"] = 0
    ddetails["dstake"] = 0.0
    ddetails["drev_cust"] = 0.0
    ddetails["dpot_cust"] = 0.0
    ddetails["dvoid"] = 0.0
    ddetails["dvoidcount"] = 0
    ddetails["dwin"] = 0
    ddetails["dlose"] = 0
    ddetails["dplace"] = 0

    for item in dataset:
        count += 1
        if item["channel"] == "M":
            mdetails["mcount"] += 1
            if item["result"] == 'W':
                mdetails["mwin"] += 1
            if item["result"] == 'L':
                mdetails["mlose"] += 1
            if item["result"] == 'P':
                mdetails["mplace"] += 1
            if item["result"] == 'V':
                mdetails["mvoid"] += float(item["stake"])
                mdetails["mvoidcount"] += 1
            else:
                mdetails["mstake"] += float(item["stake"])
                mdetails["mrev_cust"] += float(item["return"])
                mdetails["mpot_cust"] += float(item["odds"]) * float(item["stake"])
        if item["channel"] == "D":
            ddetails["dcount"] += 1
            if item["result"] == 'W':
                ddetails["dwin"] += 1
            if item["result"] == 'L':
                ddetails["dlose"] += 1
            if item["result"] == 'P':
                ddetails["dplace"] += 1
            if item["result"] == 'V':
                ddetails["dvoid"] += float(item["stake"])
                ddetails["dvoidcount"] += 1
            else:
                ddetails["dstake"] += float(item["stake"])
                ddetails["drev_cust"] += float(item["return"])
                ddetails["dpot_cust"] += float(item["odds"])*float(item["stake"])
    print(f"[-] Dataset row = {dataset[0]}")
    output = f'[-] Total data numbers are count: {count:,},'\
             f' stake: £{mdetails["mstake"]+ddetails["dstake"]:,.2f},'\
             f'return: £{mdetails["mrev_cust"]+ddetails["drev_cust"]:,.2f}'\
             ' potential: '\
             f'£{mdetails["mpot_cust"]+ddetails["dpot_cust"]:,.2f} '\
             f'void amount: £{mdetails["mvoid"]+ddetails["dvoid"]:,.2f}'\
             ' voided: '\
             f'{mdetails["mvoidcount"]+ddetails["dvoidcount"]:,} winners:'\
             f'{mdetails["mwin"]+ddetails["dwin"]:,} losers: '\
             f'{mdetails["mlose"]+ddetails["dlose"]:,} place '\
             f'{mdetails["mplace"]+ddetails["dplace"]:,}'
    print(output)
    output = f'[-] Mobile data numbers are count: {mdetails["mcount"]:,},'\
             f' stake: £{mdetails["mstake"]:,.2f}, return: '\
             f'£{mdetails["mrev_cust"]:,.2f} potential: £'\
             f'{mdetails["mpot_cust"]:,.2f} voided: '\
             f'£{mdetails["mvoid"]:,.2f} number voided'\
             f' {mdetails["mvoidcount"]:,} winners: '\
             f'{mdetails["mwin"]:,} losers: {mdetails["mlose"]:,}'\
             f' place {mdetails["mplace"]:,}'
    print(output)
    output = f'[-] Desktop data numbers are count: {ddetails["dcount"]:,},'\
             f' stake: £{ddetails["dstake"]:,.2f}, return: '\
             f'£{ddetails["drev_cust"]:,.2f} potential: £'\
             f'{ddetails["dpot_cust"]:,.2f} voided: £'\
             f'{ddetails["dvoid"]:,.2f}'\
             ' number voided '\
             f'{ddetails["dvoidcount"]:,} winners: '\
             f'{ddetails["dwin"]:,} losers:'\
             f' {ddetails["dlose"]:,} place {ddetails["dplace"]:,}'
    print(output)
    horses = gethorses(dataset)
    print(f" [-] uniques horses are {len(horses)}")
    print(f" [-] horse data is {horses['Rocky Creek']}")
    for key, item in horses.items():
        if item[1] in ('L', 'P'):
            print(f" [-] horse is {key} potential return is £{item[4]:,.2f}")
    print("[+] --- Main Function Finish")


if __name__ == '__main__':
    print("[+] - Start Grad analysis")
    main()
    print("[+] - Finish Grad analysis")
