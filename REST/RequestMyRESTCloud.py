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


# ## Running Query Mode
# count = 1
# while(True):
#     # query = {'input':input()}
#     query = {'input':randint(1000,9999)}
#     response = requests.put('http://127.0.0.1:5000', params=query)
#     print(count,"  ", response.json()['body'])
#     count+=1

# ## Cloud API GCP
# while(True):
#     query = {'input':input()}
#     response = requests.put('https://hello-world-1-s4dvklkd5a-uc.a.run.app/', params=query)
#     print(response.json()['body'])

# ## Pi 10.0.0.41
# while(True):
#     query = {'input':input()}
#     response = requests.put('http://10.0.0.41:8080', params=query)
#     print(response.json()['body'])


# ## Running Query Mode
# count = 1
# while(True):
#     # query = {'input':input()}
#     query = {'input':randint(1000,9999)}
#     response = requests.put('http://10.0.0.41:8080', params=query)
#     print(count,"  ", response.json()['body'])
#     count+=1