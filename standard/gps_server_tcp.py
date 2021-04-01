#!/usr/bin/python3

# networking
import socket
import sys

# gps_data
import gps


def gps_data():

    # Listen on port 2947 (gpsd) of localhost
    session = gps.gps("localhost", "2947")
    session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

    while True:
        try:

            report = session.next()
            # Wait for a 'TPV' report and display the current time
            # To see all report data, uncomment the line below
            # print(report)
            if report['class'] == 'TPV':

                if hasattr(report, 'time'):
                     print("\n------------------------------------------------\n")
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


def browse_menu():

    print("\n")
    print("Networking Test    - (1)")
    print("Bluetooth Services - (2)")
    print("GPS Information    - (3)")
    print("Bluetooth Connect  - (4)")
    answer = input("\nPlease select the number to test the function: \n\t- ")

    if answer == '1' :
        print ('Networking placeholder.')
    elif answer == '2' :
        scan_services()
    elif answer == '3' :
        gps_data()
    elif answer == '4' :
        bluetooth_connect()
    else:
        print("Error in choice!")

if __name__ == "__main__":

    #browse_menu()

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

            # needs to periodically send out gps/lux data to client
            package = c.recv(1024)

            print ('Receiving: {}, {}'.format(package,type(package)))

    finally:
        print ('Closing connection')
        c.close
