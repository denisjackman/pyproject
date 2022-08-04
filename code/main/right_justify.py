'''
    right justify
'''

def right_justify(item):
    '''
    return a string that is right justified so the last character of item is in column 70
    '''
    result = ""
    result = f'{item:>70}'
    return result

if __name__ == "__main__":
    print(right_justify('denis'))
