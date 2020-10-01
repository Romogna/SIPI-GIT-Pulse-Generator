# This is the client test for the IP protocol
# The final code will be write in pylon.
# Run in python, not python3

# Import socket module 
import socket
from time import sleep

# Create a socket object 
s = socket.socket()

# Define the port on which you want to connect 
port = 12345

# connect to the server on local computer 
s.connect(('pulsegenerator.local', port)) # remember to change
#192.168.0.81 - pulsegenerator

# receive data from the server 
print (s.recv(1024))

# Notes: client would send message to be parsed in testing
selection = input('Please select an option:\n 1 - Pan Right \n 2 - Pan Left \n 3 - STOP\n')

if selection == 1:
    s.send('CT,PR,63')
    sleep(1)

elif selection == 2:
    s.send('CT,PL,63')
    sleep(1)

elif selection == 3:
    s.send('CT,STOP,0')

# close the connection
s.close()
