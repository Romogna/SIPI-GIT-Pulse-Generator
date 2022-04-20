echo "Starting PIGPIO Daemon"
sudo pigpiod

echo "Starting Pulse Width Generator"
CurrentDir=$PWD

echo "Starting from $CurrentDir:"
sleep 1

echo " - PiCamera Webserver"
#python3 $CurrentDir/standard/cameraServer.py &
#sleep 1 &

echo " - Pulse Generator" &
python $CurrentDir/standard/pulse_generator.py
#python3 $CurrentDir/standard/pulse_generatorV2.py
#python $CurrentDir/standard/pulse_generator.py && fg
#python $CurrentDir/standard/copy_pulse_generator.py

echo "Closing PIGPIO Daemon"
sudo killall pigpiod
