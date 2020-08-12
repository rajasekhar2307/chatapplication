import socket
import threading 

IP = "127.0.0.1"
PORT = 7770
HEADER = 64

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((IP,PORT))


server_socket.listen()

total_sockets = [server_socket]

clients = {}

def connect_clients():
	print(f'Listening on {IP} port: {PORT}')
	while True:
		conn , addr = server_socket.accept()
		user = recv_msg(conn)
		if user is False:
			continue

		print(f'Connected with {conn}: {user["data"].decode("utf-8")}')
		total_sockets.append(conn)
		clients[conn] = user
		con_msg = 'Connected with server'
		con_msg = f'{len(con_msg):<{HEADER}}'+con_msg
		conn.send(bytes(con_msg,'utf-8'))

def recv_msg(client_socket):
	try:
		message_header = client_socket.recv(HEADER)
		if not message_header:
			return False
		message_length = int(message_header.decode('utf-8'))
		return {'header': message_header, 'data': client_socket.recv(message_length)}
	except:
		return False	


for sock in total_sockets:
	if sock == server_socket:
		connect_clients()
	else:
		message = recv_msg(sock)
		if message is False:
			print('Closed connection from: {}'.format(clients[notified_socket]['data'].decode('utf-8')))

            # Remove from list for socket.socket()
			sockets_list.remove(notified_socket)

            # Remove from our list of users
			del clients[notified_socket]

			continue

            # Get user by notified socket, so we will know who sent the message
		user = clients[notified_socket]

		print(f'Received message from {user["data"].decode("utf-8")}: {message["data"].decode("utf-8")}')

            # Iterate over connected clients and broadcast message
		for client_socket in clients:

                # But don't sent it to sender
			if client_socket != notified_socket:

                    # Send user and message (both with their headers)
                    # We are reusing here message header sent by sender, and saved username header send by user when he connected
				client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])


	