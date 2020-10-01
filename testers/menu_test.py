# This is a test to configure the control of a usb RS-232 serial adapter
# baud rate on the usb on the pi is 9600

#!/usr/bin/env python
import socket
from time import sleep
import serial

data = [] # holds parsed information


# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
	port='/dev/ttyUSB0',
	baudrate=9600
#	parity=serial.PARITY_ODD,
#	stopbits=serial.STOPBITS_TWO,
#	bytesize=serial.SEVENBITS
)

#ser.open()
#ser.isOpen()

# pelcod will receive information from package and use it to send thru serial
def pelcod(camera_options, camera_speed): # using decimal instead of hex
# sync  =           255
# addr  = camera     01
# byte3 = command1   00
# byte4 = command2   02,04, 08,16
# byte5 = pan_speed  63
# byte6 = tilt_speed 63
# checksum = calculated

    sync = 255
    camera = 01
    command1 = 0
    pan_speed = 0
    tilt_speed = 0

    if camera_options == 'PR':
      pan_speed = camera_speed
      command2 = 2

    elif camera_options == 'PL':
      pan_speed = camera_speed
      command2 = 4

    elif camera_options == 'TU':
      tilt_speed = camera_speed
      command2 = 8

    elif camera_options == 'TD':
      tilt_speed = camera_speed
      command2 = 16

    if camera_options == 'STOP':
      pan_speed = 0
      tilt_speed = 0
      command2 = 0

    checksum = (camera + command1 + command2 + pan_speed + tilt_speed) % 256

    print ('Command Sent: {},{},{},{},{},{},{}'.format(sync ,camera, command1, command2, pan_speed, tilt_speed, checksum))
    #return [camera, command1, command2, pan_speed, tilt_speed, checksum]

    command = [sync, camera, command1, command2, pan_speed, tilt_speed, checksum]

    #print (bytearray(command))

    ser.write(command)


if __name__ == "__main__":

  # next create a socket object
  s = socket.socket()
  print ('Socket successfully created')

  # reserve a port on your computer in our
  # case it is 12345 but it can be anything
  port = 12345

  # Next bind to the port
  # we have not typed any ip in the ip field
  # instead we have inputted an empty string
  # this makes the server listen to requests
  # coming from other computers on the network
  s.bind(('', port))
  print ('socket binded to {}'.format(port))

  # put the socket into listening mode
  s.listen(5)
  print ('socket is listening')

  # a forever loop until we interrupt it or
  # an error occurs
  while True:

    # Establish connection with client.
    c, addr = s.accept()
    print ('Got connection from {}'.format(addr))

    # send a thank you message to the client.
    c.send('Thank you for connecting')

    # Notes: Will do the task after receiving message
    package = c.recv(1024)
    print ('Receiving: {}, {}'.format(package,type(package)))

    data = package.split(',')

#-------------------------------------------------------
# Two options will be available
# CT - turret control signal is received
# PG - pulse signal is received


    if data[0] == 'CT':
      pelcod(data[1],int(data[2]))
      if data[1] == 'STOP':
        print ('Closing Connection')
        c.close()

#    elif data[0] == 'PG':
#      wave_creation(data[1],data[2],data[3],data[4],data[5])
#      print ('Closing Connection')
#      c.close()

    else:
      c.send('Invalid data parameters!')
      print ('invalid data')
      c.close()
#------------------------------------------------------

    # Close the connection with the client
#     print ('Closing Connection')
#     c.close()

###------End of main()----------

# Message in format "1,2,3,4,5"
# Message modified "CT,PR,3F"
# Message modified "BT,1,2,3,4,5
