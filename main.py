service = ['hostname', 'ip address', ]
toApply = []
config = open("config.txt", "a")


def service_selector():
    while 0 == 0:
        selService = str(input('What service do you need?'))
        if selService in service:
            # print(service.index(selService))
            index = int(service.index(selService))
            # print(index)
            if index == 1:
                print("ip will be assigned to vlan 1. Don't put this on a router")
            print('service supported')
            toApply.append(index)
            # print(toApply)
            toApply.sort()
        elif selService == "fin":
            break
        else:
            print('supported services include: ' + str(service))


def generate_config():
    while 0 == 0:
        if 0 in toApply:
            hostname = input("hostname ")
            config.write("\n" + hostname)
            config.close()
            toApply.remove(0)
        else:
            break


def interface_config():
    toConfig = int(input("How many interfaces to config?"))
    int(toConfig)
    for intToConfig in range(0, int(toConfig)):
        ipToAssign = input("IP address and subnet for g" + str(toConfig) + "/0")
        config.write("\n int g" + str(toConfig) + "/0 \nip address " + str(ipToAssign) + "\n exit\n")
        int(toConfig)
        toConfig -= 1


service_selector()
generate_config()
print(toApply)
configFinal = open("config.txt", "r")
contents = configFinal.read()
print(contents)
