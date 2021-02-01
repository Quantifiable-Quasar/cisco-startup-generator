service = ['hostname', 'vlan', 'interface', 'passwords', 'ssh', 'banner']
open('config.txt', 'w').close()
config = open("config.txt", "a")
selected_services = []


def hostname():
    host = input("hostname ")
    config.write("\nhostname " + host)


def vlan():
    vlan_to_config = input('How many vlans to config? ')
    while vlan_to_config != 0:
        vlan_number = str(input('Which vlan is to be configed? '))
        ip_address = str(input('enter and ip address and subnet mask to put on vlan ' + str(vlan_number) + ' '))
        config.write('\nint vlan' + str(vlan_number) + '\nip addr ' + str(ip_address) + '\nno shut\nexit\n')
        int(vlan_to_config)
        vlan_to_config = int(vlan_to_config) - 1


def interface_config():
    toConfig = int(input("How many interfaces to config?"))
    toConfig -= 1
    for intToConfig in range(-1, int(toConfig)):
        # print(toConfig)
        open('config.txt', 'r')
        ipToAssign = input("IP address and subnet for g0/" + str(toConfig) + ' ')
        # print(ipToAssign)
        config.write("\nint g0/" + str(toConfig) + "\nip address " + str(ipToAssign) + "\nno shut\nexit\n")
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
    config.write('\ncrypto key gen rsa\n' + bits)
    config.write('\nip ssh v 2\nip ssh auth 2\nip ssh time 60\n')
    telnet = input('disable telnet [y/n] ')
    if telnet == 'y':
        config.write('\nline vty 0 4\nlogin local\ntrans input ssh\nexit')


def banner():
    ban = input('banner (do not include any *) ')
    config.write('\nban motd *' + ban + '*\n')


def basic_router():
    hostname()
    interface_config()
    pass_gen()
    # need a way to have ssh have 1024 btis and telnet disabled. Maybe need to define new ssh function
    ssh()
    banner()


def basic_switch():
    hostname()
    vlan()
    pass_gen()
    ssh()
    banner()


def list_to_num():
    while 0 == 0:
        service_selection = input("What service do you need? ")
        if service_selection in service:
            print("service supported")
            index = int(service.index(service_selection))
            # print(index)
            selected_services.append(index)
            selected_services.sort()
            # print(selected_services)
        elif service_selection == 'r0':
            basic_router()
            break
        elif service_selection == 's0':
            basic_switch()
            break
        elif service_selection == 'ex':
            break
        elif service_selection == 'exit':
            break
        else:
            print("not supported")
            print("supported services are " + str(service))


def generate_config():
    while 0 == 0:
        if 0 in selected_services:
            hostname()
            selected_services.remove(0)
        elif 1 in selected_services:
            vlan()
            selected_services.remove(1)
        elif 2 in selected_services:
            interface_config()
            selected_services.remove(2)
        elif 3 in selected_services:
            pass_gen()
            selected_services.remove(3)
        elif 4 in selected_services:
            ssh()
            selected_services.remove(4)
        elif 5 in selected_services:
            banner()
            selected_services.remove(5)
        else:
            break


list_to_num()
generate_config()

config.close()
final_config = open('config.txt', 'r')
print(final_config)
line: str
for line in final_config.readlines():
    print(line)
