from socket import *
from sys import *

f=open("f.txt","r")
address=f.read(1)
f.close 

target = address

i = 6379    #---->   for a specific port
#for i in range(1,8000):
s = socket(AF_INET,SOCK_STREAM)

try:
	s.connect((target,i))
	print("Port %d is open" %i)
	s.close

except:
	print("Port %d is closed" %i)
	s.close
