# This is a test to see how the IP protocol messaging works between devices
# Code snippets are below:


###
# first of all import the socket library 
import socket

# next create a socket object 
s = socket.socket()
print "Socket successfully created"

# reserve a port on your computer in our 
# case it is 12345 but it can be anything 
port = 12345

# Next bind to the port 
# we have not typed any ip in the ip field 
# instead we have inputted an empty string 
# this makes the server listen to requests  
# coming from other computers on the network 
s.bind(('', port))
print "socket binded to %s" %(port)

# put the socket into listening mode
s.listen(5)
print "socket is listening"

# a forever loop until we interrupt it or  
# an error occurs
while True:

   # Establish connection with client. 
   c, addr = s.accept()
   print 'Got connection from', addr

   # send a thank you message to the client.  
   c.send('Thank you for connecting')

   # Notes: Will do the task after receiving message
   data = c.recv(1024)
   print('Receiving: {}, {}'.format(data,type(data)))
   data = data.split(',')
   print(data)

   for i in data:
     param[i] = int(data[i])
     print(param, type(param[i]))


   # Close the connection with the client 
   c.close()

###------

