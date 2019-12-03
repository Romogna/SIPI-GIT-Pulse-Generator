#!/usr/bin/env python

import time
import bluetooth
import pigpio

GPIO=4 # pin selected for pwg
square = []  # list to store the waveform parameters
exposure_time = [] # stores a list of exposure times
wave_param = [] # holds data from bluetooth

hostMACAddress = ''
port = 1
size = 1024

sig = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sig.bind((hostMACAddress, port))
sig.listen(1)

try:
  print("Trying")
  client_sock,address = s.accept()
  print("Accepted Connection from ", address)

  while 1:
    data = client_sock.recv(size)
    if data:
      print("Received: ", data)

  # work in this area for bluetooth parse
    
    wave_creation(wave_param)

except:
  print("Closing Socket")
  client_sock.close()
  s.close()


def wave_creation(wave_param):

#image_count = input("How many exposures will you be taking? \n")
image_count = wave_param[1]
#intial_exposure = input("Enter in the intial exposure time: ")
initial_exposure = wave_param[2]
#interval_param = input("Enter in the interval between exposures: ")
interval_param = wave_param[3]
#sequence_param = input ("Will the sequence of exposures be (geometric or arithmetic)? \n")
sequence_param = wave_param[4] # 0 is geometric, 1 is arithmetic
#sequence_steps = input ("What is the common difference/ratio? \n")
sequence_param = wave_param[5]

compile = 1
# loop to populate the exposure time list
while (compile < image_count):
  if sequence_param == 0: # will add sequence exposures to list arithmetic
    exposure_time.append(initial_exposure + (sequence_steps*compile))
  else if sequence_param == 1:  # will add sequence exposures to list geometric
    exposure_time.append(initial_exposure * (sequence_steps**compile))

  compile = compile + 1 # increment until we have enough exposures

for i in irange(0, image_count): # populates the square wave with parameters
# pulses                     ON       OFF      MICROS
  square.append(pigpio.pulse(1<<GPIO, 0,       exposure_time[i])) # varying exposures
  square.append(pigpio.pusle(0,       1<<GPIO, interval_param)) # interval between exposures

pi = pigpio.pi() # connect to local Pi
pi.set_mode(GPIO, pigpio.OUTPUT) # turns GPIO pin to output
pi.wave_add_generic(square) # adds a list(square) of pulses to current waveform
wid = pi.wave_create()  # creates a waveform with the data

if wid >= 0:
   pi.wave_send_once(wid) # generates the wave pulse
   print('Producing wave now!')
   time.sleep(10)          # used to pause time before stopping
   pi.wave_tx_stop()        # used to stop the pulse
   pi.wave_delete(wid)       # used to delete the current waveform

pi.stop()  # stops the local pi connection
