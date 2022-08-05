'''
    example
'''
grp_content = []
print(grp_content)
with open('Address_Groups.txt') as f:
    for line in f:
        if line.split(' ')[1] == "shared":
            grp_name = line.split(' ')[3]
        if '[' in line:
            content = line.split('[')[1]
            grp_content.append(content)
        else:
            content = line.split(' ')[5]
            grp_content.append(content)
print('final list : ', grp_content)
print ('list len  : ', len(grp_content))
for item in grp_content:
    print('Item    : ',item.strip())
