#server.py
import socket
# pip install uncleengineer

my_ip = '192.168.0.193'
port = 7001

while True:
	try:
		server = socket.socket()
		server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

		server.bind((my_ip,port))
		server.listen(1)

		print('Waiting for Client: ')

		client, addr = server.accept()
		print('Connect from: ',str(addr))

		data = client.recv(1024).decode('utf-8')
		print('Message from Client: ', data)

		# print("DATA TYPE: ",type(data))

		print('Data:',data)
		client.send('recieved data'.encode('utf-8'))
		client.close()
	except Exception as e:
		print("ERROR: ",e )

