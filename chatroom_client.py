
import socket
from threading import Thread
from tkinter import *
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("127.0.0.1",12340))

root = Tk()

root.title('client')

loginframe = Frame(root, width=300)
loginframe.pack()

def send_data():
    data = entry.get()
    chat = Label(root, text=data, fg='red', bg='black', anchor='e')
    chat.pack(side=TOP, fill=X)
    s.sendall(data.encode())
    entry.delete(0, END)

def login():
    global chatframe, entry
    global loginframe,label2
    e = entrylogin.get()
    s.sendall(e.encode())
    loginframe.destroy()
    chatframe = Frame(root)
    chatframe.pack(fill= BOTH,padx=10)
    entry = Entry(chatframe)
    entry.pack()
    b = Button(chatframe,text = 'send', command = send_data)
    b.pack()


def receive():
    while 1:
        data = s.recv(1024).decode()
        chat = Label(root,text = data,fg='green', bg='black', anchor='w')
        chat.pack(side= TOP,fill=X )
    s.close()

temp_thread = Thread(target = receive)
temp_thread.start()




label = Label(loginframe, text='login')
label.pack()

entrylogin = Entry(loginframe)

entrylogin.pack()

submit = Button(loginframe,text='login',command= login)
submit.pack()




root.mainloop()
