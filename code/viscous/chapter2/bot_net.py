''' Botnet simulation   '''
from pexpect import pxssh

class Client:
    ''' Client class '''

    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.session = self.connect()

    def connect(self):
        ''' connect to the host '''
        try:
            s = pxssh.pxssh()
            s.login(self.host, self.user, self.password)
            return s
        except Exception as e:
            print(e)
            print('[-] Error Connecting')
        return None

    def send_command(self, cmd):
        ''' send command to the host '''
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before

def botnet_command(command):
    ''' send command to all the bots '''
    for client in botNet:
        output = client.send_command(command)
        print('[*] Output from ' + client.host)
        print('[+] ' + output + '\n')

def add_client(host, user, password):
    ''' add a new client to the botnet '''
    client = Client(host, user, password)
    botNet.append(client)

if __name__ == '__main__':
    botNet = []
    print('[-] Botnet starting')
    add_client('10.10.10.110','root','toor')
    add_client('10.10.10.120','root','toor')
    add_client('10.10.10.130','root','toor')
    botnet_command('uname -v')
    botnet_command('cat /etc/issue')
    print('[-] Botnet complete')
