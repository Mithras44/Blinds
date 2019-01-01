#!/usr/bin/python3

import pickle


with open('blind_data.pickle', 'rb') as f:
    blind_dict = pickle.load(f)
    
message = str("Left Blind: " + str(blind_dict['left'] ) + " ¦ Middle Blind: " 
                  + str(blind_dict['middle']) + " ¦ Right Blind: " + str(blind_dict['right']))
print(message)