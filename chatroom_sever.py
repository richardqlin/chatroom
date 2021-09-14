import socket

from threading import Thread

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("0.0.0.0",12340))
s.listen(5)


connections = {}

def send_everyone(message):  
    for client in connections:
        connections[client].send(message.encode())

def listener(conn,username):

    while True:
        try:
            message = conn.recv(1024).decode()
            data = '<'+ username +">:"+ message
            send_everyone(data)
        except:
            send_everyone(username + ' has left the chat')
            del connections[username]
            return


while 1:
    conn, addr = s.accept()
    username = conn.recv(1024).decode('utf-8')
    connections[username] = conn
    #send_everyone((username + ' has joined the chat'))

    temp_thread = Thread(target = listener, args=(conn,username,))
    temp_thread.start()

