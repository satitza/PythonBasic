import socket

server_address = '192.168.2.175'
server_port = 5000

while True:
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind((server_address, server_port))
    server.listen()

    print('Server started listen port : ', str(server_port))

    client, addr = server.accept()
    print('Connect from : ', str(addr))

    data = client.recv(2048).decode('utf-8')
    print(data)

    confirm_receive = 'confirm_receive'.encode('utf-8')
    client.send(confirm_receive)
    client.close()




