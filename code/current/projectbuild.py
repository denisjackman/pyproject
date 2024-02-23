#!/usr/bin/python
'''
    OS Curl
'''
import sys
import getopt
import subprocess


def main(argv):
    '''
        main function
    '''

    try:
        opts, args = getopt.getopt(argv, 'hp:', ["project="])
    except getopt.GetoptError:
        print('oscurl.py -p <projectname>')
        sys.exit(2)
    print(args)
    for opt, arg in opts:
        if opt == '-h':
            print('oscurl.py -p <projectname>')
            sys.exit()
        elif opt in ("-p", "--project"):
            print(arg)
        else:
            print('projectbuild.py -p <projectname>')
            sys.exit()


def gettokenid():
    '''
        get token id
    '''
    # pylint: disable=C0301
    tokenid = subprocess.check_output("source ~/overcloudrc && curl -s -X "
                                      "POST $OS_AUTH_URL/tokens "
                                      "  -H \"Content-Type: application/json\""
                                      "   -d '{\"auth\": {\"t"
                                      "enantName\": \"admin\", \"passwordCred"
                                      "entials\": {\"username\": \"'\"$OS_USE"
                                      "RNAME\"'\", \"password\": \"'\"$OS_PAS"
                                      "SWORD\"'\"}}}'   | jq --raw-output .ac"
                                      "cess.token.id ",
                                      shell=True)
    examplecurl = subprocess.check_output("source ~/overcloudrc && curl -s -H"
                                          f" \"X-Auth-Token:{tokenid}"
                                          "\" http://10.236.102.21:5000/v3/en"
                                          "dpoints | python -mjson.tool")
    print(examplecurl)


if __name__ == "__main__":
    main(sys.argv[1:])
    gettokenid()
