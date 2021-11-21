import socket

server_address = '192.168.2.175'
server_port = 5000

while True:

    client = socket.socket()
    data = input('Send message to server : ')

    client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    client.connect((server_address, server_port))

    client.send(data.encode('utf-8'))

    response = client.recv(2048).decode('utf-8')
    print(response)
