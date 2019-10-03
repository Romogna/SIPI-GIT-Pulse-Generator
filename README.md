# SIPI-GIT-Pulse-Generator
Information on the SIPI-GIT pulse width generator using a raspberry pi

### PIGPIO Installation

To install the PIGPIO library, download the zip file with `wget abyz.me.uk/rpi/pigpio/pigpio.zip`.

Unzip the contents into a folder with the command `unzip pigpio.zip`.

Change directory into the PIGPIO folder created with unzip. `cd PIGPIO`

Compile the library with the `make` command.

Run the install `sudo make install`.
You will need to know the password for sudoer access.

#### Or

```

wget abyz.me.uk/rpi/pigpio/pigpio.zip
unzip pigpio.zip
cd PIGPIO
make
sudo make install

```
