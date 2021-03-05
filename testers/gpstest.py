
import gps

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
