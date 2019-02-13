#!/usr/bin/env python

'''Copyright (c) 2019 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.0 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.'''


import requests
import sys

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)




### Enter url for your environment - for example sdwan-reservable - 'https://10.10.20.90
baseurl = 'https://172.16.1.141'
url = baseurl + '/j_security_check'
data = {"j_username" : "admin", "j_password" : "admin"}
sess = requests.session()
response = sess.post(url=url, data=data, verify=False)

if response.status_code !=  200:
	print('Login Failed')
	sys.exit(0)


url = baseurl +'/dataservice/template/feature'

response = sess.get(url=url, verify=False)
listids = []
data = response.json()
for x in data['data']:
    if x['factoryDefault'] != True:

        listids.append(x['templateId'])
if listids == []:
    print('There are no custom feature Templates to delete')
    sys.exit('No Templates')

ans = input('Do you want to delete ALL custom feature Templates? Y or N')
if ans.lower() == 'y':
    print('The following templates will be deleted\n')
    for x in data['data']:
        if x['factoryDefault'] != True:
            print(x['templateName'])
    newans = input('\n Again, do you really want to delete all these feature Templates? Y or N')
    if newans.lower() == 'y':
        for x in listids:
            response = sess.delete(url=url + '/' + x)
            print(response.status_code)


