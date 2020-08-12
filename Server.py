import socket
import threading




HEADER = 10
IP = "localhost"
PORT = 7770

def conn_clients(socket):


	while True:

		conn, addr = socket.accept()
		print(f"Connection with {addr}")
		msg = "Connected with the server"
		msg = f'{len(msg):<{HEADER}}'+msg
		print(msg)

		conn.send(bytes(msg,'utf-8'))
		send_message(conn)

def send_message(conn):
	while True:
		message = input('->')

		if not message:
			return 
		message = message.encode('utf-8')
		message_header = f"{len(message):<{HEADER}}".encode('utf-8')
		conn.send(message_header + message)



def Main():

	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	server_socket.bind((IP,PORT))

	server_socket.listen()
	print(f"Listening at port {PORT}")

	clients_thread = threading.Thread(target = conn_clients, args=(server_socket,))

	clients_thread.start()
	clients_thread.join()

if __name__ == '__main__':
	Main()