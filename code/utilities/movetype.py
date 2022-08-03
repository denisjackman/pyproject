#!/usr/bin/env python
'''
    movetype
'''
print("Starting ")
filelines = [line.strip() for line in open("movies.txt","r")]
for files in filelines:
    print(files[files.find(",",1)+1:])
print("Finishing")
