#Created on 16/12/2020 by Lavinia Buleac
from socket import *
from sys import *

target = argv[1]

#i = 80    ---->   for a specific port
for i in range(1,8000):
	sock = socket(AF_INET,SOCK_STREAM)

	try:
		sock.connect((target,i))
		print("Port %d is open" %i)
		sock.close

	except:
		print("Port %d is closed" %i)
		sock.close
