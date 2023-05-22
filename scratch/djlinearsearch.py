''' linear search algorithm in python '''
## Search Algorithms - DONE
## Liner Search Algorithm - DONE
## Binary Search Algorithm
## Depth First Search Algorithm
## Breadth First Search Algorithm

## Sorting Algorithms
## insertion sort
## heap sort
## selection sort
## merge sort
## quick sort
## counting sort

def linear_search(targetlist, target):
    ''' returns the target if found, else returns None '''
    result = False
    if target in targetlist:
        for item in range(len(targetlist)):
            if targetlist[item] == target:
                return targetlist[item]
    else:
        return result

def binary_search(targetlist, low, high, target):
    ''' Binary Search Algorithm in Python '''
    result = False
    if high >= low:
        mid = (high + low) // 2
        if targetlist[mid] == target:
            return mid
        elif targetlist[mid] > target:
            return binary_search(targetlist, low, mid - 1, target)
        else:
            return binary_search(targetlist, mid + 1, high, target)
    else:
        return result

def main():
    ''' main function '''
    print("[+] Linear Search Algorithm start[+]")
    searchlist=[1,2,3,4,5,6,7,8,9,10]
    print(f'[-] Linear looking for 5 in searchlist {linear_search(searchlist, 5)}')
    print(f'[-] Linear looking for 20 in searchlist {linear_search(searchlist, 20)}')
    print(f'[-] Binary looking for 5 in searchlist {binary_search(searchlist, 0, len(searchlist)-1, 5)}')
    print(f'[-] Binary looking for 20 in searchlist {binary_search(searchlist, 0, len(searchlist)-1, 20)}')
    print("[+] Linear Search Algorithm finish[+]")

if __name__ == "__main__":
    main()
