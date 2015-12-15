# export_policies_from_srx
Exporting a policy configuration from a Juniper device to an CSV and XSL


PROBLEM OR GOAL:
How can I export a policy configuration from an SRX device to an XML-compliant spreadsheet? 

SOLUTION:
junos-device# show security policies | display xml | no-more

We can save the result to file and open in MS Exel or other application. But this format inconvenient for edit.


1) junos-device# show security policies | display xml | no-more
2) save result in file polixy.xml
3) editable in script "_address" and "_appication" dictionaries according to your configuration

    ### example 1 : if your configuration file contains 
    ### set applications application TCP_1433 protocol tcp
    ### set applications application TCP_1433 destination-port 1433
    ### set applications application TCP_1433 inactivity-timeout 43200
    ###
    ### add to _application variable "TCP_1433": "tcp/143 inactivity-timeout 43200"
    ###
    ### exaple 2: if your configuration file contains
    ### set security zones security-zone untrust address-book address NTP_1 8.8.8.8/32
    ### 
    ### add to _address variable "NTP_1": "8.8.8.8/32"
    
4) run python script export_policies_from_srx.py and get csv result


BUT WE HAVE ONE PROBLEM:
The name of source, destination and application must not contain symbol "-"


