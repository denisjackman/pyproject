''' linear search algorithm in python '''
def linear_search(targetlist, target):
    ''' returns the target if found, else returns None '''
    result = None
    if target in targetlist:
        for item in range(len(targetlist)):
            if targetlist[item] == target:
                return targetlist[item]
    else:
        return result

def main():
    ''' main function '''
    print("[+] Linear Search Algorithm start[+]")
    searchlist=[1,2,3,4,5,6,7,8,9,10]
    print(f'[-] looking for 5 in searchlist {linear_search(searchlist, 5)}')
    print(f'[-] looking for 20 in searchlist {linear_search(searchlist, 20)}')
    print("[+] Linear Search Algorithm finish[+]")

if __name__ == "__main__":
    main()
