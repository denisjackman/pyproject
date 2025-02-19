''' virtual box example'''
import virtualbox


def vbox_start(vboxs_name):
    ''' start a virtual machine '''
    vboxs = virtualbox.VirtualBox()
    vboxs_machine = vboxs.find_machine(vboxs_name)
    vboxs_session = virtualbox.Session()
    progress = vboxs_machine.launch_vm_process(vboxs_session, 'gui', [])
    progress.wait_for_completion()
    return vboxs_session


def vbox_stop(vs_session):
    ''' stop a virtual machine '''
    vs_session.console.power_down()


def main():
    ''' main function'''
    vbox = virtualbox.VirtualBox()
    print(f'VirtualBox version: {vbox.version}')
    for virtual_machine in vbox.machines:
        print(f'Virtual machine: {virtual_machine.name}')
    main_session = vbox_start("Ubuntu-Master")
    # vbox_stop(main_session)
    print(f'Virtual machine state: {main_session.console.state}')


if __name__ == '__main__':
    main()
