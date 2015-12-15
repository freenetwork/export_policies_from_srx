#!/usr/bin/python

import xml.etree.ElementTree as ET
import re
tree = ET.parse('policy.xml')
root = tree.getroot()
zone2 = []
policy2 = []
src2 = []
dst2 = []
app2 = []

_address = {"ADD1": "172.21.1.0/24", "ADD1": "172.21.6.0/24"}
_application = {"SSH": "tcp/22 inactivity-timeout 86400", "FTP": "tcp/23 inactivity-timeout 86400"}

conver_address = re.compile(r'\b(' + '|'.join(_address.keys()) + r')\b')
conver_application = re.compile(r'\b(' + '|'.join(_application.keys()) + r')\b')

print ('"SRC", "DST", "APP", "NAME", "FROM", "TO"')
for subroot in root[0]:
    for zone in subroot.findall('context-information'):
      zone2 = []
      zone2.append(zone.find('source-zone-name').text)
      zone2.append(zone.find('destination-zone-name').text)
    for policy in subroot.findall('policies'):
      policy2 = []
      src2 = []
      dst2 = []
      app2 = []
      for _policy in policy.findall('policy-information'):
         policy2.append(_policy.find('policy-name').text)
         for _a in _policy.find('source-addresses'):
            for _a_src in list(_a):
               src2.append(_a_src.text)
         for _b in _policy.find('destination-addresses'):
            for _b_src in list(_b):
               dst2.append(_b_src.text)
         for _c in _policy.find('applications'):
            for _c_app in list(_c):
               app2.append(_c_app.text)
         for each in src2:
            print '"'+conver_address.sub(lambda x: _address[x.group()], each)+'", "'+', '.join([conver_address.sub(lambda y: _address[y.group()], x) for x in dst2] )+'", '+' "'+', '.join([conver_application.sub(lambda y: _application[y.group()], x) for x in app2] )+'", '+' "'+', '.join([str(x) for x in policy2] )+'", "'+zone2[0]+'", "'+zone2[1]+'"'
