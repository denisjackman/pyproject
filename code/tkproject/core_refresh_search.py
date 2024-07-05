''' core refresh search module '''
import sys
import getopt
import csv
# import pandas as pd


def help_message():
    ''' help message '''
    print("[*] core_refresh_search.py -t"
          " <tla> REQUIRED -f <filename>"
          " REQUIRED -v True/False optional")
    print('[-] core_refresh_search ended')
    sys.exit()


def read_csv_file(rcf_filename):
    ''' read csv file '''
    rcf_result = []
    with open(rcf_filename,
              'r',
              encoding='utf-8-sig') as rcf_csvfile:
        rcf_data = csv.reader(rcf_csvfile, delimiter=',')
        for row in rcf_data:
            if row[0] != 'VMName':
                rcf_result.append(row[0])

    return rcf_result


def get_core_args(gca_argv):
    ''' get core arguments '''
    gca_verbose = False
    gca_tla = ''
    gca_filename = ''
    try:
        gc_opts, _ = getopt.getopt(gca_argv,
                                   'hvt:f:',
                                   ['help',
                                    'verbose',
                                    'tla=',
                                    'file='])
    except getopt.GetoptError as gce:
        print(f'[*] Error in get_core_args : {gce}')
        help_message()
    for gc_opt, gc_arg in gc_opts:
        if gc_opt in ('-h', '--help'):
            help_message()
        elif gc_opt in ('-v', '--verbose'):
            gca_verbose = True
        elif gc_opt in ('-t', '--tla'):
            gca_tla = gc_arg
        elif gc_opt in ('-f', '--file'):
            gca_filename = gc_arg
    return {'verbose': gca_verbose, 'tla': gca_tla, 'file': gca_filename}


def check_tla(ct_tla, ct_vmname):
    ''' check tla '''
    ct_result = False
    ct_check = ct_vmname.split('-')
    ct_temp = ct_check[1].lower()
    ct_check_tla = ''
    for ct_item in ct_temp:
        if ct_item.isdigit():
            break
        ct_check_tla += ct_item

    if ct_tla == ct_check_tla:
        ct_result = True
    return ct_result


def main():
    ''' main function '''
    print('[-] core_refresh_search started')
    main_args = get_core_args(sys.argv[1:])
    if main_args['tla'] == '':
        print('[x] TLA is missing')
        help_message()
    if main_args['file'] == '':
        print('[x] Filename is missing')
        help_message()
    main_tla = main_args['tla'].lower()
    main_filename = main_args['file']
    main_verbose = main_args['verbose']

    print('[o] TLA : {main_tla}, Filename '
          f': {main_filename}, Verbose : {main_verbose}')

    # main_df = pd.read_csv(main_filename)
    # main_tlalist = main_df.to_dict(orient='records')
    main_tlalist = read_csv_file(main_filename)
    for item in main_tlalist:
        if check_tla(main_tla, item):
            print(item)

    print('[-] core_refresh_search ended')


if __name__ == '__main__':
    main()
