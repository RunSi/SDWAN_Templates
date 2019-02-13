import requests
import sys
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

baseurl = 'https://'
url = baseurl + '/j_security_check'
data = {"j_username" : "admin", "j_password" : "admin"}
sess = requests.session()
response = sess.post(url=url, data=data, verify=False)

if response.status_code !=  200:
	print('Login Failed')
	sys.exit(0)

## Read desired template from directory featuretemplates
f=open('featuretemplates/bfd.json')
data = f.read()

data = json.loads(data)

url = baseurl _ '/dataservice/template/feature'
response = sess.post(url=url, json=data, verify=False)
if response.status_code !=  200:
	print('Create FeatureTemplates Failed. Status code = ' + str(response.status_code))
	sys.exit(0)