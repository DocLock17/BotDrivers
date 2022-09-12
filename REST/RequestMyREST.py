#!/bin/bash/python3

import requests
import pprint
from random import randint

# ## Basic Query Mode

# # query = {'input':'tofu'}
# # response = requests.put('http://127.0.0.1:5000', params=query)
# response = requests.put('http://127.0.0.1:5000', params = {'input':'tofu'})

# print(response)
# pprint.pprint(response.json())

count = 1
## Running Query Mode
while(True):
    # query = {'input':input()}
    query = {'input':randint(1000,9999)}
    response = requests.put('http://127.0.0.1:5000', params=query)
    print(count,"  ", response.json()['body'])
    count+=1

