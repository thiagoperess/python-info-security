import socket

connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Socket criado com sucesso!')

host = 'localhost'
door = 5432

connection.bind((host, door))
message = 'Servidor: Olááááá lá lá!!!'

while 1:
    data, address = connection.recvfrom(4096)

if data:
    print('Servidor enviando mensagem...')
    connection.sendto(data + (message.encode()), address)
