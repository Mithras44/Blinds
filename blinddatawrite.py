#!/usr/bin/python3

import pickle

blind_dict = {
        "left":"closed",
        "middle":"closed",
        "right": "closed"
        }


with open('blind_data.pickle', 'wb') as f:
    pickle.dump(blind_dict, f, pickle.DEFAULT_PROTOCOL)