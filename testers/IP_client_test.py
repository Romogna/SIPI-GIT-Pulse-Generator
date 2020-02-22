# This is the client test for the IP protocol
# The final code will be write in pylon, this is a testing code

# Import socket module 
import socket

# Create a socket object 
s = socket.socket()

# Define the port on which you want to connect 
port = 12345

# connect to the server on local computer 
s.connect(('192.168.0.81', port)) # remember to change
#192.168.0.81 - pulsegenerator

# receive data from the server 
print s.recv(1024)
# Notes: client would send message to be parsed in testing
s.send('1,2,3,4,5')

# close the connection 
s.close()
