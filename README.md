[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/RunSi/SDWAN_Templates)
# SD-WAN Templates

*vEdge cloud feature templates for Cisco SD-WAN*

---

## Feature and Device Template creation with SD-WAN API

To automate the process of creating SD-WAN Feature Templates in Lab environment.

This repository contains a suite of JSON Feature and Device Template payloads for Cisco SD-WAN API calls.

JSON Payloads can be modified in order to customise the templates for your particular use case.

The script [create_template.py](./create_template.py), is a very simple script to demonstrate the creation of a feature template.

### WARNING - deletetemplates.py

The script [deletetemplates.py](./deletetemplates.py) will delete all custom Feature Templates on vManage.  Use with **Extreme** caution, and do **NOT** use in production environment. 

- ### Payloads available to date

  Refer to directory [vedge_cloud_featuretemplates](./vedge_cloud_featuretemplates)

  - System vEdge
  - BFD
  - VPN vEdge
  - VPN vEdge Interface
  - OSPF
  - AAA
  - Banner
  - BGP
  - DHCP
  - IGMP
  - Multicast
  - Logging
  - NTP
  - Security
  - PIM

## Usage

Use of the templates is a two step process

**Step One**

Amend the appropriate JSON file with the parameters/variables desired, and name the Template to a name of your choice.

**Step Two**

Run the python script with the desired template .json file, e.g.

```python
python create_template.py -i 172.16.1.141 -j bfd.json
```

Alternatively, by commenting out the code at the end of the file [create_templates.py](./create_templates.py), you can load all templates within the directory - [vedge_cloud_featuretemplates](./vedge_cloud_featuretemplates) to vManage.

## Installation

Both Python 2.7 and 3.X are supported.  The only dependency is requests.  It is advisable to create a virtualenv and then run the following command:

```python
pip install -r requirements.txt
```



## Authors & Maintainers

Smart people responsible for the creation and maintenance of this project:

- Simon Hart <sihart@cisco.com>

## Credits

Help sought and received from Stuart Clark and Steven Carter - Awesome Cisco Coders - DevNet Rocks!

## License

This project is licensed to you under the terms of the [Cisco Sample
Code License](./LICENSE).
