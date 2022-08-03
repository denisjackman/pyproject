d = {1: 2, 4: 8, 7: 9}
s = 0
for x in d:
    s = s + d[x]
print(s)
print([2 * x for x in range(5) if x % 2])
l = range(5)
print(len(l))
print(l[5-1])
idx =0
lst = range(10)
if (idx >= 0) and (idx <= len(lst)):
    x = lst[idx]
