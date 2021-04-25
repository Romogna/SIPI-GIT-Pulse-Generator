#!/usr/bin/env python
import socket
import time
import serial
import pigpio

# gps_data
import gps


data = [] # holds parsed information
package = None # for holding message data till parsed


GPIO=4 # pin selected for pwg
exposure_time = [] # stores a list of exposure times
wave_param = [] # holds data from the message
square = []  # list to store the waveform parameters

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
        port='/dev/ttyUSB0',
        baudrate=9600
#       parity=serial.PARITY_ODD,
#       stopbits=serial.STOPBITS_TWO,
#       bytesize=serial.SEVENBITS
)

def gps_data():

    # Listen on port 2947 (gpsd) of localhost
    session = gps.gps("localhost", "2947")
    session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

    while True:
        try:

            report = session.next()
            if report['class'] == 'TPV':
                if hasattr(report, 'time'):
                     print("\n------------------------------------------------\n")
                     print(f'Time: {report.time} \n')

                if hasattr(report, 'alt'):
                     print(f'Altitude: {report.alt} \n')

                if hasattr(report, 'lat'):
                     print(f'Latitude: {report.lat} \n')

                if hasattr(report, 'lon'):
                     print(f'Longitude: {report.lon} \n')


            

        except KeyError:
            pass
        except KeyboardInterrupt:
            quit()
        except StopIteration:
            session = None
            print("GPSD has terminated")


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

    #print ('Command Sent: {},{},{},{},{},{},{}'.format(sync ,camera, command1, command2, pan_speed, tilt_speed, checksum$
    #return [camera, command1, command2, pan_speed, tilt_speed, checksum]

    command = [sync, camera, command1, command2, pan_speed, tilt_speed, checksum]

    #print (bytearray(command))

    ser.write(command)

#----------------end of pelcod-----------------#

def wave_creation(image_count, initial_exposure, interval_param, sequence_param, sequence_steps):

  #wave_param = data.split(',')

  #image_count = input("How many exposures will you be taking? \n")
  #image_count = int(wave_param[0])
  #intial_exposure = input("Enter in the intial exposure time: ")
  #initial_exposure = int(wave_param[1])
  #interval_param = input("Enter in the interval between exposures: ")
  #interval_param = int(wave_param[2])
  #sequence_param = input ("Will the sequence of exposures be (geometric or arithmetic)? \n")
  #sequence_param = int(wave_param[3]) # 1 is geometric, 0 is arithmetic
  #sequence_steps = input ("What is the common difference/ratio? \n")
  #sequence_steps = int(wave_param[4])

  compile = 1

  # loop to populate the exposure time list
  while (compile < image_count):
    if sequence_param == 0: # will add sequence exposures to list arithmetic
      exposure_time.append(initial_exposure + (sequence_steps*compile))
    elif sequence_param == 1:  # will add sequence exposures to list geometric
      exposure_time.append(initial_exposure * (sequence_steps**compile)) # <-needs adjustments and testing
    else:
      print ('Invalid option! Please try again.')
      exit()

    compile = compile + 1 # increment until we have enough exposures

  for i in range(0, image_count-1): # populates the square wave with parameters
  # pulses                     ON       OFF      MICROS
    square.append(pigpio.pulse(1<<GPIO, 0,       exposure_time[i])) # varying exposures
    square.append(pigpio.pulse(0,       1<<GPIO, interval_param)) # interval between exposures


  pi = pigpio.pi() # connect to local Pi
  pi.set_mode(GPIO, pigpio.OUTPUT) # turns GPIO pin to output
  pi.wave_add_generic(square) # adds a list(square) of pulses to current waveform
  wid = pi.wave_create()  # creates a waveform with the data

  if wid >= 0:
     pi.wave_send_once(wid) # generates the wave pulse
     print ('Producing wave now!')
     print (exposure_time)

     c.send('Wave produced') # send the client the wave parameters
     time.sleep(10)          # used to pause time before stopping
     pi.wave_tx_stop()        # used to stop the pulse
     pi.wave_delete(wid)       # used to delete the current waveform

     print ('Cleaning Lists')
     del exposure_time[:]    # clears the lists for the next signal
     del square[:]

  pi.stop()  # stops the local pi connection

###----- End of wave_creation()---------

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
  s.listen(1)
  print ('socket is listening')

  # a forever loop until we interrupt it or
  # an error occurs
  try:

    # Establish connection with client.
    c, addr = s.accept()
    print ('Got connection from {}'.format(addr))

    # send a thank you message to the client.
    c.send('Thank you for connecting')

    while True:

      package = c.recv(1024)

      data = package.split(',')

      print ('Receiving: {}, {}'.format(data,type(data)))

      if data[0] == 'CT':
        pelcod(data[1],int(data[2]))

      elif data[0] == 'PG':
        wave_creation(data[1],data[2],data[3],data[4],data[5])

      else:
        break

  #except KeyboardInterrupt:
    #quit()


  finally:
    print ('Closing connection')
    c.close



#------------------------------------------------------

    # Close the connection with the client
#     print ('Closing Connection')
#     c.close()

###------End of main()----------

# Message in format "1,2,3,4,5"

# Message modified "CT,PR,3F"
# Message modified "PG,1,2,3,4,5
