import socket
import threading

IP = "127.0.0.1"
PORT = 7770
HEADER = 64

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP,PORT))

username = input("Username: ")
my_username = username.encode('utf-8')
username_header = f"{len(my_username):<{HEADER}}".encode('utf-8')
client_socket.send(username_header + my_username)


def send_message():
	while True:

		message = input(f'{username} -> ')

		if message:
			message = message.encode('utf-8')
			message_header = f"{len(message):<{HEADER}}".encode('utf-8')
			client_socket.send(message_header + message)



def recieve_message():

	while True:

		username_header = client_socket.recv(HEADER).decode('utf-8')
		if not len(username_header):
			print('Connection closed by the server')
			sys.exit()

		username_length = int(username_header)
		username = client_socket.recv(username_length).decode('utf-8')

		message_header = client_socket.recv(HEADER)
		message_length = int(message_header.decode('utf-8').strip())
		message = client_socket.recv(message_length).decode('utf-8')

		print(f'{username} > {message}')

if __name__ == '__main__':

	sm_thread = threading.Thread(target = send_message)
	rv_thread = threading.Thread(target = recieve_message)

	rv_thread.start()
	sm_thread.start()

	sm_thread.join()
	rv_thread.join()