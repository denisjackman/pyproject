'''
    network py
'''
import yaml
grp_list = []
grp_list_pos = -1
grp_content = []
grp_name = []
print(grp_content)
with open('Address_Groups.txt') as f:
    for line in f:
        if line.split(' ')[1] == "shared":
            name = line.split(' ')[3]
            grp_list.append((name, []))
            if '[' in line:
                content = line.split('[')[1]
                grp_list[grp_list_pos][1].append(content)
                grp_list_pos +=1
            else:
                content = line.split(' ')[5]
                grp_list[grp_list_pos][1].append(content)
                grp_list_pos += 1

for name,content in grp_list:
    with open(f'output/{name}.yaml', 'w') as f:
        manifest = {
            'apiVersion': 'firewall.skybet.net/v1',
            'kind': 'AddressGroup',
            'metadata': {
                'name': name,
            },
            'spec': {
                'name': name,
                'members': 0,
                    'addresses': 0,
            },
        }
        for content_item in content:
            print(content_item)
            manifest['spec']['-name'] = [content]
        yaml.dump(manifest, f)