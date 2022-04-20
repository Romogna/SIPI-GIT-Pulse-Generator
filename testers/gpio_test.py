#!/usr/bin/env python

import time

import pigpio

GPIO=4 # pin selected for pwg

square = []  # list to store the waveform parameters
exposure_time = [] # stores a list of exposure times


image_count = input("How many exposures will you be taking? \n")
print("All time entries are in milliseconds(ms) \n")
intial_exposure = input("Enter in the intial exposure time: ")
interval_param = input("Enter in the interval between exposures: ")
sequence_param = input ("Will the sequence of exposures be (geometric or arithmetic)? \n")
sequence_steps = input ("What is the common difference/ratio? \n")

# test code begin "Do Not Run"

compile = 0

# loop to populate the exposure time list
while (compile < image_count):
  if compile == 0:  # intial exposure is at the front of the list
    exposure_time.append(intial_exposure)
  elif sequence_param == "arithmetic": # will add sequence exposures to list
    exposure_time.append(intial_exposure + (sequence_steps*compile))
  elif sequence_param == "geometric":  # will add sequence exposures to list
    exposure_time.append(intial_exposure * (sequence_steps**compile))

  compile = compile + 1 # increment until we have enough exposures

for i in irange(0, image_count):
  square.append(pigpio.pulse(1<<GPIO, 0,       exposure_time[i])) # varying exposures
  square.append(pigpio.pusle(0,       1<<GPIO, interval_param)) # interval between exposures

# test code end

# pulses                   ON       OFF    MICROS
#square.append(pigpio.pulse(1<<GPIO, 0,       10))
#square.append(pigpio.pulse(0,       1<<GPIO, 10))

pi = pigpio.pi() # connect to local Pi

pi.set_mode(GPIO, pigpio.OUTPUT) # turns GPIO pin to output

pi.wave_add_generic(square) # adds a list(square) of pulses to current waveform

wid = pi.wave_create()  # creates a waveform with the data

if wid >= 0:
   pi.wave_send_once(wid) # repeats the wave pulse
   print('Producing wave now!')
   time.sleep(10)          # used to time of the pulsing before stopping
   pi.wave_tx_stop()        # used to stop the pulse
   pi.wave_delete(wid)       # used to delete the current waveform


pi.stop()  # stops the local pi connection

#Todo
# Make a way to count the number of pulses, and duration
# pi.callback(GPIO)
