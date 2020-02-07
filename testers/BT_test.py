# Test script to understand bluetooth communications

import bluetooth

hostMACAddress = ''
port = 1
size = 1024

s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.bind((hostMACAddress, port))
s.listen(1)


try:
  print("Trying")
  client_sock,address = s.accept()
  print("Accepted Connection from ", address)

  while 1:
    data = client_sock.recv(size)
    if data:
      print("Received: ", data)

except:
  print("Closing Socket")
  client_sock.close()
  s.close()
