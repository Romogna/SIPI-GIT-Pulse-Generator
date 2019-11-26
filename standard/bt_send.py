import bluetooth

serverMACAddress = 'B8:27:EB:9B:73:91'
port = 1

s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.connect((serverMACAddress, port))

s.send("hello world")

print("finished")

s.close()
