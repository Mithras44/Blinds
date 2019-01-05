# Blinds
Python scripts to run on a raspberry pi in order to turn window blinds into either an open or closed position.

The current setup is with three blinds.

## Hardware

* 3 x MCU DIY 28BYJ-48 4 Phase Stepper Motor 5V with UL2003 Driver Board

## Create Pickle file

The first step is to create a pickle file with blinds postition set in either the open or the closed position.

Open the **blinddatawrite.py** file, change accordingly and then run.

You can verfify the file you create by running **blinddataread.py**.

## Install and setup Mosquito Server

You can then setup a MQTT mosquito server using instructions from:
```
sudo apt-get install mosquitto
sudo apt-get install mosquitto-clients
```
* https://www.youtube.com/watch?v=AsDHEDbyLfg 
* https://medium.com/@eranda/setting-up-authentication-on-mosquitto-mqtt-broker-de5df2e29afc

It is recommended that you create a username and password for your mosquito server.

## Install Paho Client 

You then need to install the paho python client libraries with the commands:
```
pip install paho-mqtt
```

## Setup python files 

Add the mosquto server's details to the **blind_paho.py** file.

Add the correct pin's and required turning time for each blind to **blindssh.py** file.

## Setup Cronjob

You can set the python script to start on reboot using these cronjon commands:
https://www.raspberrypi.org/documentation/linux/usage/cron.md 

Add:
```
@reboot python3 /home/pi/blind_paho.py &
```

## Control blinds

To control the blinds, you can either use an app such as :
https://play.google.com/store/apps/details?id=snr.lab.iotmqttpanel.prod

Or run a tkinter GUI on a computer using the **blind_tkinter.py** script.
