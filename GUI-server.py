from tkinter import *
############
import socket
import threading
serverip = '192.168.0.100'
port = 9000

def Runserver():
    while True:
        server = socket.socket()
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

        server.bind((serverip, port))
        server.listen(1)
        print('waiting....')

        # ตอบรับการเชื่อมต่อ
        client, addr = server.accept()
        print(client, addr)

        # รับค่า
        data = client.recv(1024).decode('utf-8')
        print('Data from client:',data)

        # ดึงค่าเก่ามา
        oldtext = v_result.get()
        newtext = oldtext + '\n' + data
        v_result.set(newtext)

        # ตอบกลับ ต้อง encode
        text_response = 'recieved'.encode('utf-8')
        client.send(text_response)
        # ปิดการเชื่อมต่อ
        client.close()

def ThreadRunserver():
    task = threading.Thread(target=Runserver)
    task.start()


############
GUI = Tk() #โปรแกรมหลัก
GUI.geometry('800x500')
GUI.title('โปรแกรมมอนิเตอร์ ข้อความ')

L = Label(GUI, text='โปรแกรมมอนิเตอร์ข้อความ', font=('Angsana New',30,'bold'))
L.pack() #นำไปติดกับโปรแกรมหลัก

v_result = StringVar() #ตัวแปรพิเศษใช้แสดงผลข้อความจาก client
v_result.set('---------Result---------')
R1 = Label(GUI, textvariable=v_result, justify=LEFT)
R1.place(x=10,y=50)



ThreadRunserver() #เริ่มต้นทำงานฟังชั่น thread
GUI.mainloop()