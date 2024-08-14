'''example port scan'''
import sys
import argparse


def main():
    '''main function'''
    parser = argparse.ArgumentParser(usage='djex.py -H TARGET_HOST -p TARGET_PORTS')
    parser.add_argument('-H', metavar='TARGET_HOST', type=str, help='specify target host')
    parser.add_argument('-p', metavar='TARGET_PORT', type=str, help='specify target port[s] separated by comma')
    args = parser.parse_args()
    args.tgtHost = str(args.H)
    args.tgtPorts = str(args.p).split(',')
    if (args.tgtHost is None) | (args.tgtPorts[0] is None):
        print(parser.usage)
        sys.exit(0)


if __name__ == '__main__':
    main()
