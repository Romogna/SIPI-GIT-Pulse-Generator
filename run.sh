
echo "Starting PIGPIO Daemon"
sudo pigpiod

echo "Starting Pulse Width Generator"
python3 standard/gpio_test.py

echo "Closing PIGPIO Daemon"
sudo killall pigpiod
