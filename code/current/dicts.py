''' dicts.py '''
d = {1: 2, 4: 8, 7: 9}
S = 0
for x, y in d.items():
    S = S + y
print(S)
print([2 * x for x in range(5) if x % 2])
llcoolj = range(5)
print(len(llcoolj))
print(llcoolj[5-1])
IDX = 0
lst = range(10)
if 0 <= IDX <= len(lst):
    x = lst[IDX]
