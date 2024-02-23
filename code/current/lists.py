'''
    lists.py
'''
lst = [1, 82, -6, 4, 3, 8]
print(lst[2])
print(lst[-1])
print(4 in lst)
print(lst.index(8))
print(lst.index(4))
print(lst)
lst.append(632)
print(lst)
print(lst.pop())
print(lst)
print(lst.pop(4))
print(lst)
if 4 in lst:
    lst.remove(4)
print(lst)
