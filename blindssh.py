#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
import pickle
import atexit

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

leftturns = 3000 # change value 
middleturns = 3000 # change value
rightturns = 2400 # change value
sec = 7 # change value
sec_delay = int(sec) / 1000.0

leftpin1 = 2 # change value
leftpin2 = 3 # change value
leftpin3 = 4 # change value
leftpin4 = 17 # change value

middlepin1 = 27 # change value
middlepin2 = 22 # change value
middlepin3 = 10 # change value
middlepin4 = 9 # change value

rightpin1 = 11 # change value
rightpin2 = 25 # change value
rightpin3 = 8 # change value
rightpin4 = 7 # change value

leftbutton = 24 # change value - not yet used
middlebutton = 23 # change value - not yet used
rightbutton = 18 # change value - not yet used
allopenbutton = 15 # change value - not yet used
allclosedbutton = 14 # change value - not yet used


GPIO.setup(leftpin1, GPIO.OUT)
GPIO.setup(leftpin2, GPIO.OUT)
GPIO.setup(leftpin3, GPIO.OUT)
GPIO.setup(leftpin4, GPIO.OUT)

GPIO.setup(middlepin1, GPIO.OUT)
GPIO.setup(middlepin2, GPIO.OUT)
GPIO.setup(middlepin3, GPIO.OUT)
GPIO.setup(middlepin4, GPIO.OUT)

GPIO.setup(rightpin1, GPIO.OUT)
GPIO.setup(rightpin2, GPIO.OUT)
GPIO.setup(rightpin3, GPIO.OUT)
GPIO.setup(rightpin4, GPIO.OUT)

forward_seq = ['1001', '1000', '1100', '0100', '0110', '0010', '0011', '0001']
reverse_seq = list(forward_seq) # to copy the list
reverse_seq.reverse()

blind_dict = None


def write_pickle(blind_dict=blind_dict):
    with open('blind_data.pickle', 'wb') as f:
        pickle.dump(blind_dict, f, pickle.DEFAULT_PROTOCOL)

def read_pickle():
    with open('blind_data.pickle', 'rb') as f:
        blind_dict = pickle.load(f)
        return blind_dict


def turning(delay, steps, sequence, set_step):
  for i in range(steps):
    for step in sequence:
      set_step(step)
      time.sleep(delay)


def left_set_step(step):
	GPIO.output(leftpin1, step[0] == '1')
	GPIO.output(leftpin2, step[1] == '1')
	GPIO.output(leftpin3, step[2] == '1')
	GPIO.output(leftpin4, step[3] == '1')

def middle_set_step(step):
	GPIO.output(middlepin1, step[0] == '1')
	GPIO.output(middlepin2, step[1] == '1')
	GPIO.output(middlepin3, step[2] == '1')
	GPIO.output(middlepin4, step[3] == '1')

def right_set_step(step):
	GPIO.output(rightpin1, step[0] == '1')
	GPIO.output(rightpin2, step[1] == '1')
	GPIO.output(rightpin3, step[2] == '1')
	GPIO.output(rightpin4, step[3] == '1')

	
def leftblindopening():
    blind_dict = read_pickle()
    left_set_step('0000')
    turning(sec_delay, int(leftturns), reverse_seq, left_set_step)
    left_set_step('0000')
    blind_dict['left'] = "open"
    print(blind_dict['left'])
    write_pickle(blind_dict)

def leftblindclosing():
    blind_dict = read_pickle()
    left_set_step('0000')
    turning(sec_delay, int(leftturns), forward_seq, left_set_step)
    left_set_step('0000')
    blind_dict['left'] = "closed"
    print(blind_dict['left'])
    write_pickle(blind_dict)

def middleblindopening():
    blind_dict = read_pickle()
    middle_set_step('0000')
    turning(sec_delay, int(middleturns), reverse_seq, middle_set_step)
    middle_set_step('0000')
    blind_dict['middle'] = "open"
    print(blind_dict['middle'])
    write_pickle(blind_dict)

def middleblindclosing():
    blind_dict = read_pickle()
    middle_set_step('0000')
    turning(sec_delay, int(middleturns), forward_seq, middle_set_step)
    middle_set_step('0000')
    blind_dict['middle'] = "closed"
    print(blind_dict['middle'])
    write_pickle(blind_dict)
 
def rightblindopening():
    blind_dict = read_pickle()
    right_set_step('0000')
    turning(sec_delay, int(rightturns), reverse_seq, right_set_step)
    right_set_step('0000')
    blind_dict['right'] = "open"
    print(blind_dict['right'])
    write_pickle(blind_dict)

def rightblindclosing():
    blind_dict = read_pickle()
    right_set_step('0000')
    turning(sec_delay, int(rightturns), forward_seq, right_set_step)
    right_set_step('0000')
    blind_dict['right'] = "closed"
    print(blind_dict['right'])
    write_pickle(blind_dict)


def leftblindturn():
	blind_dict = read_pickle()
	if blind_dict["left"] == "closed":
		leftblindopening()
	elif blind_dict["left"] == "open":
		leftblindclosing()

def middleblindturn():
	blind_dict = read_pickle()
	if blind_dict["middle"] == "closed":
		middleblindopening()
	elif blind_dict["middle"] == "open":
		middleblindclosing()

def rightblindturn():
	blind_dict = read_pickle()
	if blind_dict["right"] == "closed":
		rightblindopening()
	elif blind_dict["right"] == "open":
		rightblindclosing()

def allopen():
	blind_dict = read_pickle()
	if blind_dict["left"] == "closed":
		leftblindopening()
	if blind_dict["middle"] == "closed":
		middleblindopening()
	if blind_dict["right"] == "closed":
		rightblindopening()

def allclosed():
	blind_dict = read_pickle()
	if blind_dict["left"] == "open":
		leftblindclosing()
	if blind_dict["middle"] == "open":
		middleblindclosing()
	if blind_dict["right"] == "open":
		rightblindclosing()

    
def gpio_close():
    GPIO.cleanup()

atexit.register(gpio_close)
