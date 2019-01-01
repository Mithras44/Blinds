# Blinds
Python scripts to run on a raspberry pi in order to turn window blinds.

First step is to create pickle file with blinds in either open or closed position.

Open the blinddatawrite.py file, change accordingly and then run.

You can verfify the file you create by running blinddataread.py

You can then setup a MQTT mosquito server using instructions from:

sudo apt-get install mosquitto
sudo apt-get install mosquitto-clients

https://www.youtube.com/watch?v=AsDHEDbyLfg 

It is recommended that you create a username and password for your mosquito server.

You then need to install the paho python client libraries with the commands:

pip install paho-mqtt

You can set the python script to start on reboot using these cronjon commands:
https://www.raspberrypi.org/documentation/linux/usage/cron.md 

To control the blinds, you can either use an app such as :
https://play.google.com/store/apps/details?id=snr.lab.iotmqttpanel.prod

Or create run a tkinter GUI on a computer using the blind_tkinter.py script.
