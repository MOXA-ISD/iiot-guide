# RESTful API

### Requirements/Constraints in ThinsPro v2.0
- A valid access token 
>obtained through ThingsPro web consule using the root accont
- URL Structure
> https://<ipaddress>/api/v1/<resource>


## RESTful API via Python
```
$ sudo pip install requests
$ ./<filename>.py
```

|          | Description      | Program                      |
| -------- | ---------------- | ---------------------------- |
| 001      | System Status    | 001-system-resource.py       |
| 002      | Network Status   | 002-network-resource.py      |
| 003      | DNS Status       | 003-dns-resource.py          |
| 004      | Ethernet Status  | 004-ethernets-resource.py    |
| 005      | Generic MQTT     | 005-generic-mqtt-resource.py |
