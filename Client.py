import socket
import threading

HEADER = 10



c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(('localhost',7770))


while True:
	nmsg = ''
	flag = True
	while True:
		msg = c.recv(HEADER).decode('utf-8')
		if flag:
			msglen = int(msg)
			flag = False
		
		nmsg = nmsg + msg

		if len(nmsg)- HEADER == msglen:
			print(nmsg[HEADER:])
			flag = True
			nmsg = ''


