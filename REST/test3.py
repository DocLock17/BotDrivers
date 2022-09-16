#!/bin/bash/python3

# Try import and install inline if module import fails.
import sys
import subprocess
import pkg_resources

required  = {'requests'} 
installed = {pkg.key for pkg in pkg_resources.working_set}
missing   = required - installed

if missing:
    # implement pip as a subprocess:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', *missing])

import requests



# Set API endpoint and query and response fields
api_endpoint = 'http://35.188.177.166:5000'
query_field = 'input'
response_field = 'body'


# Set a count variable for bug tracking.
count = 1


# Send REST input based requests in an infinite loop print response and increment count variable for tracking.
while(True):
  query = {query_field:input("Enter input to query field: {0} \nFor request to: {1} \n".format(query_field, api_endpoint))}
  print(query)
  response = requests.put(api_endpoint, json=query)
  print('\n ',count,"  ", response.json()[response_field], '\n')
  count+=1