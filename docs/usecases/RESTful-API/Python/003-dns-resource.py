#!/usr/bin/env python3

import requests

headers  = {
        "mx-api-token": "$2a$10$PcsmSox/LU5.iq1k20lh9.eQoBcFrT0GBONtbtNVSkjwm4kmtNC2O",
        "Content-Type": "application/json" }

r = requests.get(
        'https://192.168.5.127/api/v1/network/dns',
        headers = headers,
        verify = False
        )

dns = {
        "dns": ["8.8.8.8", "8.8.4.4"],
        "enableFixed": False,
        "fixedDns": ["208.67.222.222", "208.67.222.220"],
        }

p = requests.put(
        'https://192.168.5.127/api/v1/network/dns',
        headers = headers,
        json = dns,
        verify = False
        )

getdata = r.json()
putdata = p.json()

print(getdata)
print(putdata)
