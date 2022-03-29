import socket

serverip = '192.168.0.100'
port = 9000

while True:
    data = input('Send to server: ')
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    server.connect((serverip,port))

    # ส่งข้อความ
    server.send(data.encode('utf-8'))

    # รับข้อความตอบกลับจาก server
    data_server = server.recv(1024).decode('utf-8')
    print('Data from server: ',data_server)
    server.close()