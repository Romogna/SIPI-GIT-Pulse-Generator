#!/usr/bin/python3


import gps
import bluetooth


def scan_services():

    print("Scanning for bluetooth devices: ")
    devices = bluetooth.discover_devices(lookup_names = True)
    number_of_devices = len(devices)
    print(number_of_devices, "devices found")

    for addr,name in devices:

      print("\n")
      print("Device Name: %s" % (name))
      print("Device MAC Address: %s" % (addr))
      print("Services Found:")
      services = bluetooth.find_service(address=addr)

      if len(services) <=0:

          print("zero services found on", addr)

      else:

          for serv in services:

              print(serv['name'])

      print("\n")

    return()


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


def bluetooth_connect():

    # establish a communication socket on RFCOMM
    server_socket=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
    port = 1
    server_socket.bind(("",port))
    server_socket.listen(1)
    client_socket,address = server_socket.accept()

    print("Accepted connection from ",address)


    while True:
        res = self.client_socket.recv(1024)
        client_socket.send(res)
        if res == 'q':
            print ("Quit")
            break
        else:
            print("Received:",res)

    client_socket.close()
    server_socket.close()

def browse_menu():

    print("\n")
    print("Bluetooth Scanner  - (1)")
    print("Bluetooth Services - (2)")
    print("GPS Information    - (3)")
    print("Bluetooth Connect  - (4)")
    answer = input("\nPlease select the number to test the function: \n\t- ")

    if answer == '1' :
        scan()
    elif answer == '2' :
        scan_services()
    elif answer == '3' :
        gps_data()
    elif answer == '4' :
        bluetooth_connect()
    else:
        print("Error in choice!")

if __name__ == "__main__":

    browse_menu()
