#!/usr/bin/env python3

import requests

headers = { 
        "mx-api-token": "$2a$10$PcsmSox/LU5.iq1k20lh9.eQoBcFrT0GBONtbtNVSkjwm4kmtNC2O",
        "Content-Type": "application/json" }

r = requests.get(
        'https://192.168.5.127/api/v1/network/ethernets',
        headers = headers,
        verify = False)

data = r.json()

print(data)
