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
import json
import argparse

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# parser = argparse.ArgumentParser('template parser')
# parser.add_argument('-i', action="store", dest="hostname", help="enter host or ip address")
# parser.add_argument('-j', action="store", dest="filejson", help="enter json file for template")
# args= parser.parse_args()


### Enter url for your environment - for example sdwan-reservable - 'https://10.10.20.90
def main():
    baseurl = 'https://'+host
    url = baseurl + '/j_security_check'
    data = {"j_username" : "admin", "j_password" : "admin"}
    sess = requests.session()
    response = sess.post(url=url, data=data, verify=False)

    if response.status_code !=  200:
        print('Login Failed ')
        sys.exit(0)

    ## Read desired template from directory vedge_cloud_featuretemplates
    with open('vedge_cloud_featuretemplates/'+jsonfile) as f:
        data = f.read()
        data = json.loads(data)

    url = baseurl + '/dataservice/template/feature'
    response = sess.post(url=url, json=data, verify=False)
    if response.status_code !=  200:
        print('Create FeatureTemplates Failed. Status code = ' + str(response.status_code) )
        print(response.text)
        sys.exit(0)
    else:
        print('Template '+args.filejson+' succesfully deployed to vManage')

### Below, if uncommented will create all feature templates in the vedge_cloud_featuretemplates
# payloads = os.listdir('vedge_cloud_featuretemplates')
# url = baseurl +'/dataservice/template/feature'
# for x in payloads:
# 	print(x)
# 	f=open('vedge_cloud_featuretemplates/' + x)
# 	data = f.read()
# 	data = json.loads(data)
# 	response = sess.post(url=url, json=data, verify=False)
# 	if response.status_code != 200:
# 		print('Create FeatureTemplates Failed. Status code = ' + str(response.status_code))
# 	else:
# 		print('successfully loaded payload '+x)

if __name__ == '__main__':
    parser = argparse.ArgumentParser('template parser')
    parser.add_argument('-i', action="store", dest="hostname", help="enter host or ip address")
    parser.add_argument('-j', action="store", dest="filejson", help="enter json file for template")
    args = parser.parse_args()
    host = args.hostname
    jsonfile = args.filejson
    main()