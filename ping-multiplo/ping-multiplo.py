import os
from time import sleep

with open('./ping-multiplo/hosts.txt') as file:
    dump = file.read()
    dump = dump.splitlines()

    for ip in dump:
        print('Verificando o ip: ', ip)
        os.system(f'ping -n 2 {ip}')
        sleep(1)
