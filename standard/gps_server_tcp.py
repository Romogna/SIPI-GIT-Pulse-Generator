#!/usr/bin/python3

# networking
import socket
import sys

# gps_data
import gps
import time

def gps_data():

    gps_time = None
    gps_speed = None
    gps_climb = None
    gps_alt = None
    gps_lat = None
    gps_lon = None

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
                     #print("\n------------------------------------------------\n")
                     #print(f'Time: {report.time} \n')
                     gps_time = str(report.time)

                if hasattr(report, 'speed'):
                     #print(f'Speed: {report.speed * gps.MPS_TO_KPH} \n')
                     gps_speed = str(report.speed * gps.MPS_TO_KPH)

                if hasattr(report, 'climb'):
                     #print(f'Climb: {report.climb} \n')
                     gps_climb = str(report.climb)

                if hasattr(report, 'alt'):
                     #print(f'Altitude: {report.alt} \n')
                     gps_alt = str(report.alt)

                if hasattr(report, 'lat'):
                     #print(f'Latitude: {report.lat} \n')
                     gps_lat = str(report.lat)

                if hasattr(report, 'lon'):
                     #print(f'Longitude: {report.lon} \n')
                     gps_lon = str(report.lon)


                # Section to create and send data
                package = gps_time + ',' + gps_speed + ',' + gps_alt + ',' + gps_lat + ',' + gps_lon + '\n'
                #print ('1 -> {}, {}'.format(package,type(package)))
                #package.encode()
                print ('2 -> {}, {}'.format(package.encode(),type(package.encode())))
                c.send(package.encode())
            time.sleep(0.5)

        except StopIteration:
            session = None
            print("GPSD has terminated")


if __name__ == "__main__":

    #browse_menu()

    # next create a socket object
    s = socket.socket()
    print ('Socket successfully created')

    # reserve a port on your computer in our
    # case it is 12345 but it can be anything
    port = 9010

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
        #message = 'Thank you for connecting'

        #byt = message.encode()
        #c.send(byt)

        while True:

            # needs to periodically send out gps/lux data to client
            gps_data()

            #package = c.recv(1024)
            #package.decode()
            #print ('Receiving: {}, {}'.format(package,type(package)))

    finally:
        print ('Closing connection')
        c.close
