''' This is a play area to test ideas and concepts'''
def remove_identical_items(list1, list2):
    """Compares two lists looking for identical items and removes all the items from one of the lists that are identical, leaving you with a list of unique items.
        Args:
        list1 (list): The first list to compare.
        list2 (list): The second list to compare.

    Returns:
        list: A list of unique items, containing the items that are present in either list1 or list2, but not both.
    """
    # Create a new list to store the unique items.
    unique_items = []
    # Iterate through the first list.
    for item in list1:
    # If the item is not present in the second list, add it to the unique items list.
        if item not in list2:
            unique_items.append(item)
    # Return the list of unique items.
    return unique_items

def main():
    ''' main function '''
    # Example usage:
    list1 = [1, 2, 3, 4, 5]
    list2 = [2, 4, 6, 7, 8]
    # Remove all the items from list1 that are also present in list2.
    unique_items = remove_identical_items(list1, list2)
    # Print the list of unique items.
    print(f'[-] The first list {list1}')
    print(f'[-] The Second list {list2}')
    print(f'[-] The unique items{unique_items}')
    unique_items += remove_identical_items(list2, list1)
    print(f'[-] The unique items{unique_items}')

if __name__ == '__main__':
    print('[=] playtime starting up')
    main()
    print('[=] playtime shutting down')
