import socket

connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Cliente socket criado com sucesso!')

host = 'localhost'
door = 5433
message = 'Olá servidor, serenão?'

try:

    print(f'Cliente: {message}')
    connection.sendto(message.encode(), (host, 5432))

    data, server = connection.recvfrom(4096)
    data = data.decode()
    print(f'Cliente: {data}')

finally:

    print(f'Cliente fechando a conexão')
    connection.close()