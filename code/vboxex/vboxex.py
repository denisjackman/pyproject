''' virtual box example'''
import virtualbox


def main():
    ''' main function'''
    vbox = virtualbox.VirtualBox()
    print(f'VirtualBox version: {vbox.version}')
    for virtual_machine in vbox.machines:
        print(f'Virtual machine: {virtual_machine.name}')


if __name__ == '__main__':
    main()
