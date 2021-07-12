import socket
import sys

def main():
    try:
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

    except socket.error as erro:
        print('A conexão falhou!')
        print(f'Erro {erro}')
        sys.exit()

    print('Socket criado com sucesso!')

    target_host = input('Digite o Host ou IP a ser conectado: ')
    target_door = input('Digite a porta a ser conectada: ')

    try:
        connection.connect((target_host, int(target_door)))
        print(f'Cliente TCP conectado com sucesso no host {target_host}')
        connection.shutdown(2)

    except socket.error as erro:

        print(f'Não foi possível conectar ao Host {target_host}!')
        print(f'Erro {erro}')
        sys.exit()

if __name__ == '__main__':
    main()
    