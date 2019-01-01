# -*- coding: utf-8 -*-

import tkinter
from tkinter import ttk
import paho.mqtt.client as mqtt

broker_ip = # input ip address of mosquito server 
broker_user = # input user of mosquito server 
broker_password = # input pasword of mosquito server 
broker_port = # input port of mosquito server

StatusConnect = "Connecting"


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected with result code " + str(rc))
        client.subscribe("blind/left")
        client.subscribe("blind/middle")
        client.subscribe("blind/right")
        client.subscribe("blind/all_open")
        client.subscribe("blind/all_closed")
        client.subscribe("blind/status")
        StatusLabel['text'] = StatusConnect
    else:
        print("Can't connect because of error code : " + str(rc))


def on_message(client, userdata, msg):
    global StatusText
    print(msg.topic+" "+str(msg.payload.decode("utf-8")))
    if msg.topic == "blind/status":
        StatusLabel['text'] = str(msg.payload.decode("utf-8"))


def LeftFunction():
    print('Turn Left Blind')
    client.publish("blind/left", "turn", qos=0, retain=False)


def MiddleFunction():
    print('Turn Middle Blind')
    client.publish("blind/middle", "turn", qos=0, retain=False)


def RightFunction():
    print('Turn Right Blind')
    client.publish("blind/right", "turn", qos=0, retain=False)


def AllOpenFunction():
    print('Turn All Blinds Open')
    client.publish("blind/all_open", "turn", qos=0, retain=False)


def AllClosedFunction():
    print('Turn All Blinds Closed')
    client.publish("blind/all_closed", "turn", qos=0, retain=False)


def when_quit():
    client.loop_stop()
    client.disconnect()
    print('MQTT client disconnected, exiting now.')
    window.destroy()


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
# client.on_publish = on_publish

client.username_pw_set(broker_user, broker_password)
client.connect(broker_ip, broker_port, 60)

# Tkinter element

window = tkinter.Tk()


MyTitle = tkinter.Label(window,
                        text="Blind Turner",
                        font="Helvetica 16 bold")
MyTitle.pack(padx=15, pady=10, anchor="w")

# window.iconbitmap(r'blind_icon.ico')

StatusLabel = ttk.Label(window, text=StatusText)

ButtonLeft = tkinter.Button(window, text="Left", command=LeftFunction)

ButtonMiddle = tkinter.Button(
    window, text="Middle", command=MiddleFunction)

ButtonRight = tkinter.Button(
    window, text="Right", command=RightFunction)

ButtonAllOpen = tkinter.Button(
    window, text="All Open", command=AllOpenFunction)

ButtonAllClosed = tkinter.Button(
    window, text="All Closed", command=AllClosedFunction)


StatusLabel.pack(padx=8, pady=2, anchor="w")
ButtonLeft.pack(padx=15, pady=15, anchor="w")
ButtonMiddle.pack(padx=15, pady=10, anchor="w")
ButtonRight.pack(padx=15, pady=10, anchor="w")
ButtonAllOpen.pack(padx=15, pady=10, anchor="w")
ButtonAllClosed.pack(padx=15, pady=10, anchor="w")

client.loop_start()

window.protocol("WM_DELETE_WINDOW", when_quit)
window.mainloop()
