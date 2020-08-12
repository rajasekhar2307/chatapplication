import socket
import threading




HEADER = 10
IP = "localhost"
PORT = 7770


connections = []

def conn_clients(socket):


	while True:

		conn, addr = socket.accept()
		connections.append(conn)
		print(f"Connection with {addr}")
		msg = "Connected with the server"
		print(f'Active Conn: {len(connections)-1}')
		msg = f'{len(msg):<{HEADER}}'+msg
		

		conn.send(bytes(msg,'utf-8'))
		
		sm_thread = threading.Thread(target = send_message, args=(conn,))
		recv_thread = threading.Thread(target = recieve_message, args=(conn,))
		sm_thread.start()
		recv_thread.start()		

		

def send_message(conn):
	while True:
		message = input('->')

		if not message:
			return 
		message = message.encode('utf-8')
		message_header = f"{len(message):<{HEADER}}".encode('utf-8')
		conn.send(message_header + message)

def recieve_message(socket):
	while True:
		message_header = socket.recv(HEADER).decode('utf-8')
		if message_header:
			message_length = int(message_header)
			message = socket.recv(message_length).decode('utf-8')
			print(message)



def Main():

	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connections.append(server_socket)
	server_socket.bind((IP,PORT))

	server_socket.listen()
	print(f"Listening at port {PORT}")

	conn_clients(server_socket)



if __name__ == '__main__':
	Main()