from tkinter import *
from tkinter import ttk # theme of Tk
from tkinter import simpledialog 

#################
import socket
import threading
serverip = '192.168.0.100'
port = 9000

#################

GUI = Tk()
GUI.geometry('800x400')
GUI.title('โปรแกรมส่งข้อความไปหา Server')

v_username = StringVar()
v_username.set('--Username--')
Luser = Label(GUI, textvariable=v_username,font=(None,18))
Luser.place(x=650,y=10)

# ช่องกรอกข้อความ #Entry
v_message = StringVar()
E1 = ttk.Entry(GUI,textvariable=v_message ,width=30 ,font=(None,20))
E1.pack(pady=30)

# ปุ่มกดส่งข้อความ

def SendMessage(data):
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    server.connect((serverip, port))

    # ส่งข้อความ
    server.send(data.encode('utf-8'))

    # รับข้อความตอบกลับจาก server
    data_server = server.recv(1024).decode('utf-8')
    print('Data from server: ',data_server)
    server.close()

def ButtonSend(event=None):
    msg = '{}|{}'.format(v_username.get(), v_message.get())
    task = threading.Thread(target=SendMessage, args=[msg])
    task.start()
    v_message.set('') #clear ข้อความที่พิมพ์

E1.bind('<Return>', ButtonSend)

B1 = ttk.Button(GUI,text='Send',command=ButtonSend)
B1.pack(ipadx=30,ipady=20)

# ถาม username


text = simpledialog.askstring('ชื่อผู้ใช้งาน','กรุณากรอกชื่อผู้ใช้งาน')
print(text)
v_username.set(text)

GUI.mainloop()