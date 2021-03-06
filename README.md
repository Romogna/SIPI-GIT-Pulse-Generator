# SIPI-GIT-Pulse-Generator
Information on the SIPI-GIT pulse width generator using a raspberry pi

### Updating Libraries

Before you begin, you may want to update your system and python library.
```
sudo apt-get update
sudo apt-get install pigpio python-pigpio python3-pigpio
```

If the Python install fails it may be because you need the setup tools.

`sudo apt install python-setuptools python3-setuptools`

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

Make sure to run the python scripts with the `python` command and not `python3`.

After installing PIGPIO Library, change the run.sh file to be executable.

`chmod +x run.sh`

Run the program by using `./run.sh`

Notes:
```
sudo apt-get update
sudo apt-get install python-pip python-dev ipython

sudo apt-get install bluetooth libbluetooth-dev
sudo pip install pybluez

```
