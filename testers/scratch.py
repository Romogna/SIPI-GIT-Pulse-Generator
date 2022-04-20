import serial

try:
  ser = serial.Serial(
      port='/dev/ttyUSB0',
      baudrate=9600
  )

finally:
  print ('Closing')
