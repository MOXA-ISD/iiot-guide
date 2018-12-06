# Upgrade Debian Packages

The following instruction is an example for upgrding Debian packages on UC-8112-ME series. For more infomation, please refer to [UC-8100-LX Software User's Manual (for Debian 8)](https://www.moxa.com/doc/man/UC-8100_Series_LinuxSW_UM_e3.0_Debian8.pdf#page=66)

## General (system-wide) Upgrade
1. Update the Debian package lists

```
moxa@Moxa:~$ sudo apt-get update
```

2. Perform the upgrade command

```
moxa@Moxa:~$ sudo apt-get upgrade
```

Review the output messages and type "y" to confirm.

## Upgrade a specific Debian package

1. Update the Debian package lists

    ```
    moxa@Moxa:~$ sudo apt-get update
    ```

1. Query the version information, confirm you could get the latest version on moxa reposiroty.

        moxa@Moxa:~$ sudo apt-cache policy uc8100me-syskernel
        uc8100me-syskernel:
            Installed: 2.3.0+memory
            Candidate: 2.3.1
            Version table:
                2.3.1 0
                500 http://debian.moxa.com/debian/ jessie/main armhf Packages
            *** 2.3.0+memory 0
                100 /var/lib/dpkg/status
                2.1.0 0
                500 http://debian.moxa.com/debian/ jessie/main armhf Packages

    > In above case, we are trying to upgrade package "uc8100me-syskernel" and you can see the **Installed**, **Candidate** version is different. Candidate version is the one when we trying to install from remote what we will get.

1. Update a package by name

    ```
    moxa@Moxa:~$ sudo apt-get install uc8100me-syskernel
    ```

    Here is the example output

        Reading package lists... Done
        Building dependency tree
        Reading state information... Done
        The following packages will be upgraded:
            uc8100me-syskernel
        1 upgraded, 0 newly installed, 0 to remove and 71 not upgraded.
        Need to get 9,780 kB of archives.
        After this operation, 414 kB disk space will be freed.
        Get:1 http://debian.moxa.com/debian/ jessie/main uc8100me-syskernel armhf 2.3.1 [9,780 kB]
        Fetched 9,780 kB in 10s (911 kB/s)
        (Reading database ... 25723 files and directories currently installed.)
        Preparing to unpack .../uc8100me-syskernel_2.3.1_armhf.deb ...
        Unpacking uc8100me-syskernel (2.3.1) over (2.3.0+memory) ...
        Setting up uc8100me-syskernel (2.3.1) ...
        *** System successfully updated. ***
        *** Please reboot the system...***

    As you can see, `Unpacking uc8100me-syskernel (2.3.1) over (2.3.0+memory) ...`. Now the package version of `uc8100me-syskernel` is `2.3.1` instead of the old version.

1. Reboot

1. Verify upgraded version (optional)

        moxa@Moxa:~$ dpkg -l | grep uc8100me-syskernel
        ii  uc8100me-syskernel            2.3.1                            armhf        Linux kernel modules on UC-8112-ME series

    If the installation isn't success, the `ii` will be something else.
