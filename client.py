import socket
import threading

HEADER = 10





def recieve_message(connection):
	while True:
		message_header = connection.recv(HEADER).decode('utf-8')
		if message_header:
			message_length = int(message_header)
			message = connection.recv(message_length).decode('utf-8')
			print(message)


def send_message(connection):
	while True:
		message = input('->')

		if not message:
			return 
		message = message.encode('utf-8')
		message_header = f"{len(message):<{HEADER}}".encode('utf-8')
		connection.send(message_header + message)



def Main():

	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client_socket.connect(('localhost',7770))

	rv_thread = threading.Thread(target = recieve_message, args=(client_socket,))
	sm_thread = threading.Thread(target = send_message, args=(client_socket,))
	rv_thread.start()
	sm_thread.start()

if __name__ == '__main__':
	Main()