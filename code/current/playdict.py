'''
    This is a dictionary update script project.
    It is used to update the dictionary
'''

playdict = {"test": [1, 2, 3], "test2": [1, 1, 1]}


def main():
    ''' main function '''
    print("[+] -- Main Function Start")
    test_list = [{'gfg': 1, 'is': 2}, {'best': 1, 'for': 3}, {'CS': 2}]
    print(f"The original list : {test_list}")
    res = list(set(val for dic in test_list for val in dic.values()))
    print(f"The unique values in list are : {res}")
    print("[+] -- Main Function End")


if __name__ == "__main__":
    main()
