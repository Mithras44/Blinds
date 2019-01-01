# Blinds
Python scripts to run on a raspberry pi in order to turn window blinds.

First step is to create pickle file with blinds in either open or closed position.

You can then setup a MQTT mosquito server using instructions from:

You then need to install the paho client libraries with the commands:

You can set the python script to start on reboot using htese cronjon commands:

To control the blinds, you can either use an app such as :

Or create run a tkinter GUI on a computer using the blind_tkinter.py script.
