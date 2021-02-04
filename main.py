from __future__ import annotations

# __future__ maintain compatibility with lower python versions.

"""
This program generates cisco configuration files
"""

# Output filename
output_filename = "config.txt"

# Available Services
service = ['hostname', 'ip address', 'interface', 'passwords', 'ssh', 'banner']

# Creates the config file and creates an open file referents
config = open(output_filename, "w")

# Holds selected servcies
selected_services = []


def format_command(string: str) -> str:
    """
    Adds new line to the end of each command
    """
    return string + "\n"


def service_hostname():
    """
    Configures hostname
    """

    host = input("hostname ")
    config.write("\nhostname " + host)


def service_vlan():
    """
    Configures vlan
    """
    while True:
        vlan = input("which vlan to config? ")
        if vlan != 'ex':
            ip_address = input("ip to assign to vlan " + str(vlan))
            config.write('\nint vlan' + str(vlan) +
                         '\nip addr ' + ip_address + '\nno shut\nexit')
        else:
            break


def service_interface():
    """
    Configures interface
    """
    toConfig = int(input("How many interfaces to config?"))
    for intToConfig in range(-1, int(toConfig)):
        # print(toConfig)
        # open('config.txt', 'r')
        ipToAssign = input(
            "IP address and subnet for g0/" + str(toConfig) + ' ')
        # print(ipToAssign)
        config.write("\nint g0/" + str(toConfig) +
                     "\nip address " + str(ipToAssign) + "\nno shut\nexit\n")
        int(toConfig)
        toConfig -= 1


def service_password():
    """
    Configures passwords
    """
    execPass = input("Exec mode pass ")
    config.write('\nenable pass ' + execPass)
    execSec = input('Exec mode secret ')
    config.write('\nenable sec ' + execSec)
    lineconPass = input('linecon pass ')
    config.write('\nline con 0\npass ' + lineconPass + '\nlogin\nexit')


def service_ssh():
    """
    Configures ssh

    """
    domain = input('define a domain name ')
    config.write('\nip domain-name ' + domain)
    ssh_user = input('ssh username ')
    ssh_pass = input('ssh pass ')
    config.write('\nusername ' + str(ssh_user) + ' pass ' + str(ssh_pass))
    bits = str(input("how many bits to gen for rsa key? "))
    config.write('\ncry key gen rsa\n' + bits)
    config.write('\nip ssh v 2\nip ssh auth 2\nip ssh time 60\n')
    telnet = input('disable telnet [y/n] ')
    if telnet == 'y':
        config.write('\nline vty 0 4\nlogin local\ntrans input ssh')


def service_banner():
    """
    Configures banners 
    """
    ban = input('banner (do not include any *) ')
    config.write('\nban motd *' + ban + '*\n')


def generate_config():
    """
    Generates selected configs
    """
    while True:
        if 0 in selected_services:
            service_hostname()
            selected_services.remove(0)
        elif 1 in selected_services:
            service_vlan()
            selected_services.remove(1)
        elif 2 in selected_services:
            service_interface
            selected_services.remove(2)
        elif 3 in selected_services:
            service_password
            selected_services.remove(3)
        elif 4 in selected_services:
            service_ssh
            selected_services.remove(4)
        elif 5 in selected_services:
            service_banner()
            selected_services.remove(5)
        else:
            break


def main():
    while True:

        # Select service
        service_selection = input("What service do you need? ")

        # Check if selceted servies exists
        if service_selection in service:
            print("service supported")
            index = int(service.index(service_selection))
            # print(index)
            # Add selected service to list
            selected_services.append(index)
            selected_services.sort()
            # print(selected_services)
        elif service_selection.strip().lower() == 'quit':
            # Configure selected servies
            break
        else:
            print("not supported")
            print("supported services are " + str(service))


if __name__ == "__main__":
    main()
    generate_config()
    config.close()
