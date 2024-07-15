'''
    file handling
'''
# open a file and read it in stripping the newline out of it
with open('Z:/Resources/text/shipnames.txt',
          'r',
          encoding='utf-8-sig') as fileline:
    for line in fileline:
        lines = line.strip()

# open file
with open('Z:/Resources/text/shipnames.txt',
          "r",
          encoding='utf-8-sig') as f:
    # read it in
    slines = f.readlines()

print(lines)
print(len(lines))
print(type(lines))

print(slines)
print(len(slines))
print(type(slines))
