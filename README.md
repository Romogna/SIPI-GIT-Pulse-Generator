# SIPI-GIT-Pulse-Generator
Information on the SIPI-GIT pulse width generator using a raspberry pi

### Updating Libraries

Before you begin, you may want to update your system and python library.
```
sudo apt-get update
sudo apt-get install pigpio python-pigpio python3-pigpio
```

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
### Running Generator

After installing PIGPIO Library, change the run.sh file to be executable.

`chmod +x run.sh`

Run the program by using `./run.sh`
