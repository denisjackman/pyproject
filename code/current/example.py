'''
    suffixes
'''
from __future__ import annotations
from myfunctions.memsizes import approximate_size

if __name__ == '__main__':
    print(approximate_size(1000000000000, False))
    print(approximate_size(1000000000000))
