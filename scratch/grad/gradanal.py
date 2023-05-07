'''
    grad analysis script
'''
import csv

DATA_FILE = "y:/pyproject/data/GN-2016-sample-data.csv"

def opengradfile(csvfilename):
    ''' open csv file and send it back as a list '''
    csvlist = []
    result =  []
    print("[+] --- Start Open CSV File ")
    with open(csvfilename, 'r', encoding="utf-8-sig") as csvfile:
        csvlist = csv.DictReader(csvfile, delimiter=",")
        for row in csvlist:
            result.append(row)
    print("[+] --- Finish Open CSV File ")
    return result

def gethorses(horselist):
    ''' return the dict of horse '''
    result = {}
    #for horse in horselist:
    print("[+] --- Start Get Horse")
    for item in horselist:
        if item["horse"] not in result:
            hpotreturn = float(item["odds"])*float(item["stake"])
            result[item["horse"]] = [item["horse"],item["result"], float(item["stake"]), float(item["return"]), hpotreturn, float(item["freebet_amount"]), 1]
        else:
            hstake = result[item["horse"]][2] + float(item["stake"])
            hreturn = result[item["horse"]][3] + float(item["return"])
            hpotreturn = result[item["horse"]][4] + float(item["odds"])*float(item["stake"])
            hfreebet = result[item["horse"]][5] + float(item["freebet_amount"])
            hcount = result[item["horse"]][6] + 1
            result[item["horse"]] = [item["horse"], item["result"], hstake, hreturn, hpotreturn, hfreebet, hcount]
    print("[+] --- Finish Get Horse")
    return result

def main():
    ''' main function '''
    print("[+] -- Main Function Start")
    dataset = opengradfile(DATA_FILE)
    print(f"[+] Number of items in dataset is {len(dataset)}")
    count = 0
    mcount = 0
    mstake = 0.0
    mrev_cust = 0.0
    mpot_cust = 0.0
    mvoid = 0.0
    mvoidcount = 0
    mwin = 0
    mplace = 0
    mlose = 0

    dcount = 0
    dstake = 0.0
    drev_cust = 0.0
    dpot_cust = 0.0
    dvoid = 0.0
    dvoidcount = 0
    dwin = 0
    dlose = 0
    dplace = 0

    for item in dataset:
        count += 1
        if item["channel"] == "M":
            mcount +=1
            if item["result"] == 'W':
                mwin += 1
            if item["result"] == 'L':
                mlose += 1
            if item["result"] == 'P':
                mplace += 1
            if item["result"] == 'V':
                mvoid += float(item["stake"])
                mvoidcount += 1
            else:
                mstake += float(item["stake"])
                mrev_cust += float(item["return"])
                mpot_cust += float(item["odds"])*float(item["stake"])
        if item["channel"] =="D":
            dcount +=1
            if item["result"] == 'W':
                dwin += 1
            if item["result"] == 'L':
                dlose += 1
            if item["result"] == 'P':
                dplace += 1
            if item["result"] == 'V':
                dvoid += float(item["stake"])
                dvoidcount += 1
            else:
                dstake += float(item["stake"])
                drev_cust += float(item["return"])
                dpot_cust += float(item["odds"])*float(item["stake"])
    print(f"[-] Dataset row = {dataset[0]}")
    output = f"[-] Total data numbers are count: {count:,}, stake: £{mstake+dstake:,.2f},"\
             f"return: £{mrev_cust+drev_cust:,.2f} potential: £{mpot_cust+dpot_cust:,.2f} "\
             f"void amount: £{mvoid+dvoid:,.2f} voided: {mvoidcount+dvoidcount:,} winners:"\
             f"{mwin+dwin:,} losers: {mlose+dlose:,} place {mplace+dplace:,}"
    print(output)
    output = f"[-] Mobile data numbers are count: {mcount:,}, stake: £{mstake:,.2f}, return: "\
             f"£{mrev_cust:,.2f} potential: £{mpot_cust:,.2f} voided: £{mvoid:,.2f} number voided"\
             f" {mvoidcount:,} winners: {mwin:,} losers: {mlose:,} place {mplace:,}"
    print(output)
    output = f"[-] Desktop data numbers are count: {dcount:,}, stake: £{dstake:,.2f}, return: "\
             f"£{drev_cust:,.2f} potential: £{dpot_cust:,.2f} voided: £{dvoid:,.2f} number voided "\
             f"{dvoidcount:,} winners: {dwin:,} losers: {dlose:,} place {dplace:,}"
    print(output)
    horses = gethorses(dataset)
    print(f" [-] uniques horses are {len(horses)}")
    print(f" [-] horse data is {horses['Rocky Creek']}")
    for key, item in horses.items():
        if item[1] in ('L','P'):
            print(f" [-] horse is {key} potential return is £{item[4]:,.2f}")
    print("[+] --- Main Function Finish")


if __name__ == '__main__':
    print("[+] - Start Grad analysis")
    main()
    print("[+] - Finish Grad analysis")
