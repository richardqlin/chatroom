import socket

import threading

host = '0.0.0.0'

port = 9999

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((host,port))

s.listen(5)

clients = []

clients_dict={}
nicknames = []

def broadcast(message):
    print(clients)
    for client in clients:

        client.send(message)

def handle(client):
    while 1:
        try:
            message = client.recv(1024)
            print(nicknames[clients.index(client)])

            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname= nicknames[index]
            nicknames.remove(nickname)
            break


def receive():
    while 1:
        client, address = s.accept()
        print('Connection with',address,client)


        client.send(''.encode('utf-8'))
        nickname = client.recv(1024)
        print('nickname',nickname)

        nicknames.append(nickname)
        clients.append(client)

        print('clients',clients_dict)

        print('Nick name of the client is', nickname)
        broadcast(f"{nickname} connected to the server\n".encode('utf-8'))
        client.send('Connect to the server'.encode('utf-8'))

        thread = threading.Thread(target=handle, args = (client,))
        thread.start()

receive()
print('sever run')
