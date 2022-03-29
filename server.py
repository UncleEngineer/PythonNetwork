# server.py

import socket

serverip = '192.168.0.100'
port = 9000

while True:
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

    server.bind((serverip,port))
    server.listen(1)
    print('waiting....')

    # ตอบรับการเชื่อมต่อ
    client, addr = server.accept()
    print(client, addr)

    # รับค่า
    data = client.recv(1024).decode('utf-8')
    print('Data from client:',data)

    # ตอบกลับ ต้อง encode
    text_response = 'recieved'.encode('utf-8')
    client.send(text_response)
    # ปิดการเชื่อมต่อ
    client.close()
