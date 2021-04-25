
import gps
import bluetooth

import os
import sys


# Listen on port 2947 (gpsd) of localhost
session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)



def main(argv):

	if len(argv) < 2:
		print_help()
		exit(1)

	server_bt_port = int(argv[1])

	server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

	server_bt_address = '', server_bt_port

	server_sock.bind(server_bt_address)
	server_sock.listen(1)

	while True:

		client_sock,address = server_sock.accept()
		print('Accepted connection from ', address)

		data = client_sock.recv(1024)
		print('Received: ' + data.decode('utf-8'))

		client_sock.close()

	server_sock.close()


while True:

    try:

        report = session.next()
        # Wait for a 'TPV' report and display the current time
        # To see all report data, uncomment the line below
        # print(report)
        if report['class'] == 'TPV':

             #print(report)

            if hasattr(report, 'time'):
                 print(f'Time: {report.time} \n')

            if hasattr(report, 'speed'):
                 print(f'Speed: {report.speed * gps.MPS_TO_KPH} \n')

            if hasattr(report, 'climb'):
                 print(f'Climb: {report.climb} \n')

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


if _name_ == '_main_':

    main(sys.argv)
