service = ['hostname', 'ip address', 'interface', 'passwords', 'ssh', 'banner']
config = open("config.txt", "a")


def hostname():
    host = input("hostname ")
    config.write("\nhostname " + host)


def ip_address():
    ip_addr = input('enter and ip address and subnet mask to put on vlan 1')
    config.write('\nint vlan1\nip addr ' + ip_addr + '\nexit\n')


def interface_config():
    toConfig = int(input("How many interfaces to config?"))
    for intToConfig in range(-1, int(toConfig)):
        print(toConfig)
        open('config.txt', 'r')
        ipToAssign = input("IP address and subnet for g" + str(toConfig) + "/0 ")
        print(ipToAssign)
        config.write("\nint g" + str(toConfig) + "/0 \nip address " + str(ipToAssign) + "\nexit\n")
        int(toConfig)
        toConfig -= 1
def pass_gen():
    execPass = input("Exec mode pass ")
    config.write('\nenable pass ' + execPass)
    execSec = input('Exec mode secret ')
    config.write('\nenable sec ' + execSec)
    lineconPass = input('linecon pass ')
    config.write('\nline con 0\npass ' + lineconPass + '\nlogin\nexit')


def ssh():
    domain = input('define a domain name ')
    config.write('\nip domain-name ' + domain)
    ssh_user = input('ssh username ')
    ssh_pass = input('ssh pass ')
    config.write('\nusername ' + str(ssh_user) + ' pass ' + str(ssh_pass))
    bits = str(input("how many bits to gen for rsa key? "))
    config.write('\ncry key gen rsa ' + bits)
    config.write('\nip ssh v 2\nip ssh auth 60\nip ssh time 60\n')
    telnet = input('disable telnet [y/n] ')
    if telnet == 'y':
        config.write('\nline vty 0 4\nlogin local\ntrans input ssh')


def banner():
    ban = input('banner (do not include any *) ')
    config.write('ban motd *' + ban + '*\n')


def gen_conf():
    while 0 == 0:
        toApply = input('select a service or type ? for more options ')
        if toApply == 'hostname':
            hostname()
        elif toApply == 'ip address':
            ip_address()
        elif toApply == 'interface':
            interface_config()
        elif toApply == 'pass':
            pass_gen()
        elif toApply == 'ssh':
            ssh()
        elif toApply == 'banner':
            banner()
        elif toApply == '?':
            print(service)
        elif toApply == 'ex':
            break
        else:
            print('not supported')


gen_conf()
config.close()
