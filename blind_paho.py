#!/usr/bin/python3

import paho.mqtt.client as mqtt
from blindssh import *
import atexit
import RPi.GPIO as GPIO

broker_ip = # input ip address of mosquito server 
broker_user = # input user of mosquito server 
broker_password = # input pasword of mosquito server 
broker_port = # input port of mosquito server

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
   print("Connected with result code "+str(rc))
   client.subscribe("dev/test")
   client.subscribe("blind/left")
   client.subscribe("blind/middle")
   client.subscribe("blind/right")
   client.subscribe("blind/all_open")
   client.subscribe("blind/all_closed")
   client.subscribe("blind/status")
   publish_count = 0
   if publish_count == 0:
       client.publish("blind/status",str(blind_status_message()), qos=0, retain=True)
       publish_count = 1

 # Subscribing in on_connect() - if we lose the connection and
 # reconnect then subscriptions will be renewed.
 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload.decode("utf-8")))
    if msg.topic == "blind/left" and str(msg.payload.decode("utf-8")) == str("turn"):
        print("to turn left blind ")
        leftblindturn()
        print("status is : " + str(blind_status_message()))
        client.publish("blind/status",str(blind_status_message()), qos=0, retain=True)
    if msg.topic == "blind/middle" and str(msg.payload.decode("utf-8")) == str("turn"):
        print("to turn middle blind")
        middleblindturn()
        print("status is : " + str(blind_status_message()))
        client.publish("blind/status",str(blind_status_message()), qos=0, retain=True)
    if msg.topic == "blind/right" and str(msg.payload.decode("utf-8")) == str("turn"):
        rightblindturn()
        print("status is : " + str(blind_status_message()))
        client.publish("blind/status",str(blind_status_message()), qos=0, retain=True)
    if msg.topic == "blind/all_open" and str(msg.payload.decode("utf-8")) == str("turn"):
        allopen()
        print("status is : " + str(blind_status_message()))
        client.publish("blind/status",str(blind_status_message()), qos=0, retain=True)
    if msg.topic == "blind/all_closed" and str(msg.payload.decode("utf-8")) == str("turn"):
        allclosed()
        print("status is : " + str(blind_status_message()))
        client.publish("blind/status",str(blind_status_message()), qos=0, retain=True)

def blind_status_message():
    blind_dict = read_pickle()
    message = str("Left Blind: " + str(blind_dict['left'] ) + " ¦ Middle Blind: " 
                  + str(blind_dict['middle']) + " ¦ Right Blind: " + str(blind_dict['right']))
    return message

def exiting():
    GPIO.cleanup()
    client.disconnect()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
#client.on_publish = on_publish

client.username_pw_set(broker_user,broker_password)
client.connect(broker_ip, broker_port, 60)

try:
    client.loop_forever()
except KeyboardInterrupt:
    GPIO.cleanup()
    client.disconnect()
    print('MQTT client disconnected, exiting now.')
finally:
    exiting()

atexit.register(exiting)
