#!/usr/bin/env python3
"""
A minimum of one tag must be selected prior enabling!!!
"""

import requests

headers  = {
        "mx-api-token": "$2a$10$PcsmSox/LU5.iq1k20lh9.eQoBcFrT0GBONtbtNVSkjwm4kmtNC2O",
        "Content-Type": "application/json" }

mqtt = {
        "test":[],
        "TLS": False,
        "certificatefilename":"",
        "retain": False,
        "qos":"2", #QoS
        "sentbychange": True,
        "topic":"00:90:e8:00:ee:88",
        "lastwillmessage":"",
        "password":"",
        "keepalive":"60",
        "lastwilltopic":"",
        "payloadtype":"2", #Payload Type
        "clientid":"00:90:e8:00:ee:88", #Payload Topic
        "Advanced": False,
        "port":"1883", #MQTT Port
        "targethost":"iot.eclipse.com", #Broker's Address
        "maxstoredays":"Forever",
        "cleansession": True,
        "rootcafilename":"",
        "log_on_dis": False,
        "8883port":"8883",
        "log_dist":"/var/mxc",
        "cloud_conn_status": False, 
        "privatekeyfilename":"",
        "username":"",
        "enable": False, #Enable
        "log_dist_opts":["/var/mxc"],
        "maxstorage":100,
        "lastwillqos":"0",
        "lastwillretain": False }

p = requests.put(
        'https://192.168.5.127/api/v1/iot/mqtt',
        headers = headers,
        json = mqtt,
        verify = False)

pushdata = p.json()

