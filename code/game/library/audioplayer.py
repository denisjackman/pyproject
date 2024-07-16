"""
    audioplayer.py
    This is the main source.
    This is a tool for viewer images.
"""

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 1.0 $"
__date__ = "$Date: 2019/09/24 00:00:00 $"
__copyright__ = "Copyright (c) 2018 Denis J Jackman"
__license__ = "Python"

import os

CAPTION = "audioplayer"


def main():
    '''
        main routine
    '''
    target = ".wav"
    directory = 'Z:/Resources/sounds'
    file_list = []
    for filename in os.listdir(directory):
        if filename.endswith(target):
            file_list.append(os.path.join(directory, filename))

    for _ in file_list:
        print(_)


if __name__ == '__main__':
    main()
