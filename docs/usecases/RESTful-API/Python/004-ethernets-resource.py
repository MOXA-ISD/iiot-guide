#! /usr/bin/env python3

import requests

headers  = {
        "mx-api-token": "$2a$10$PcsmSox/LU5.iq1k20lh9.eQoBcFrT0GBONtbtNVSkjwm4kmtNC2O",
        "Content-Type": "application/json" }

"""
r = requests.get(
        'https://192.168.5.127/api/v1/network/ethernets',
        headers = headers,
        verify = False
        )
"""

ethernets = [{
        #eth0 settings
        "mode":"static",
        "status": False,
        "netmask":"255.255.240.0",
        "subnet":"192.168.112.0",
        "gateway":"192.168.127.1",
        "enable": True,
        "enableDhcp": False,
        "name":"eth0",
        "ip":"192.168.119.5"
        ,"wan": True,
        "id":1,
        "broadcast":"192.168.127.255",
        "mac":"00:90:e8:00:ee:88",
        "dns":["8.8.8.8","8.8.4.4"],
        "type":"eth"
        }, {
        #eth1 settings
        "mode":"static",
        "status": False,
        "netmask":"255.255.255.0",
        "wan": False,
        "ip":"192.168.4.127",
        "mac":"00:90:e8:00:ee:89",
        "subnet":"192.168.4.0",
        "enable": True,
        "gateway":"192.168.4.254",
        "name":"eth1",
        "id":2,
        "broadcast":"192.168.4.255",
        "enableDhcp": False,
        "dns":[],
        "type":"eth"}]

p = requests.put(
        'https://192.168.5.127/api/v1/network/ethernets',
        headers = headers,
        json = ethernets,
        verify = False
        )

# getdata = r.json()
putdata = p.json()

# print(getdata)
print(putdata)
