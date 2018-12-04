# Install IoT Edge on UC-8100-ME (Debian 8)

## Install IoT Edge

```shell
#!/bin/bash

# 0. Install curl
sudo apt-get update && sudo apt-get install -y curl

# 1. Download and install the moby-engine
curl -L https://aka.ms/moby-engine-armhf-latest -o moby_engine.deb && sudo dpkg -i ./moby_engine.deb

# 2. Download and install the moby-cli
curl -L https://aka.ms/moby-cli-armhf-latest -o moby_cli.deb && sudo dpkg -i ./moby_cli.deb

# 3. Download and install the standard libiothsm implementation
curl -L https://aka.ms/libiothsm-std-linux-armhf-latest -o libiothsm-std.deb && sudo dpkg -i ./libiothsm-std.deb

# 4. Download and install the IoT Edge Security Daemon
curl -L https://aka.ms/iotedged-linux-armhf-latest -o iotedge.deb && sudo dpkg -i ./iotedge.deb

# 5. Install Libssl1.0.2 (only for Debian 8)

if [ "$(hostnamectl | grep -c jessie)" -eq 1 ]; then
    curl -L http://ftp.us.debian.org/debian/pool/main/o/openssl1.0/libssl1.0.2_1.0.2l-2+deb9u3_armhf.deb -o libssl1.0.2_1.0.2l-2+deb9u3_armhf.deb && sudo dpkg -i ./libssl1.0.2_1.0.2l-2+deb9u3_armhf.deb
fi

# 6. Run apt-get fix
sudo apt-get install -f
```

## Update configuration (Required, only for Debian 8)

If you are running IoT Edge on Debian 8, you will have to modify the `config.yaml` file for resolving systemd compatibility issue. More info: https://github.com/Azure/iotedge/issues/14
 
1. File `/etc/iotedge/config.yaml` and change the listen addresses to `fd://0` and `fd://1`

```
listen:
  management_uri: "fd://0"
  workload_uri: "fd://1"
```

2. And type `systemctl daemon-reload` then `systemctl restart iotedge`


## Docker configuration (Optional)

Edit the file: `/etc/docker/daemon.json`, with the following content:

```
{
  "graph": "/var/lib/docker",
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "10m",
    "max-file": "2"
  }
}
```

- Logging: By default, there is no limitation for docker logging size, number of files.
- Change default path from `/var/lib/docker` to somwhere else
    - If you are running docker on a constrained embedded computer, you might want to move the Docker directory from the default one to somewhere else (e.g. SD card)
