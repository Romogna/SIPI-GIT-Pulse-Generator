#!/usr/bin/env python

import time

import pigpio

GPIO=21 # pin selected for pwg

square = []  # list to store the waveform parameters

on_Input = input("How long is the up in microseconds? ")
off_Input = input("How long is the down in microseconds? ")

# pulses                   ON       OFF    MICROS
square.append(pigpio.pulse(1<<GPIO, 0,       on_Input))
square.append(pigpio.pulse(0,       1<<GPIO, off_Input))

pi = pigpio.pi() # connect to local Pi

pi.set_mode(GPIO, pigpio.OUTPUT) # turns GPIO pin to output

#pi.set_pull_up_down(GPIO, pigpio.PUD_OFF)

pi.wave_add_generic(square) # adds a list(square) of pulses to current waveform

wid = pi.wave_create()  # creates a waveform with the data

if wid >= 0:
   pi.wave_send_repeat(wid) # repeats the wave pulse
   print('Producing wave now!')
   time.sleep(50)          # used to time of the pulsing before stopping
   pi.wave_tx_stop()        # used to stop the pulse
   pi.wave_delete(wid)       # used to delete the current waveform
   print('Wave has ended.')

pi.stop()  # stops the local pi connection

#Todo
# Make a way to count the number of pulses, and duration
# pi.callback(GPIO)
