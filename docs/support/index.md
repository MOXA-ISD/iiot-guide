# Support

- For techicanl issues, please [contact Moxa TS Team](https://www.moxa.com/support/request_support.aspx) by moxa.com directly.

- For product information, please find your [local sales representatives](https://www.moxa.com/where_to_buy/search.aspx).

## FAQ

### 1. How to get model name?

Type the following command:

```sh
moxa@Moxa:~$ kversion -a
UC-8112-ME-T-LX version 2.2 Build 18010313
```

It shows `UC-8112-ME-T-LX` with platform version 2.2 build `18010313`

### 2. How to get ThingsPro version?

```sh
moxa@Moxa:~$ pversion
UC-8112-ME-T-LX-CG version 2.3 Build 18033000
```

It shows ThingsPro version 2.3 build `18033000`

> If the unit complains about "Can't find the command", it means you don't have ThingsPro installed on this unit.


## Known Issues

Here are the known issues for ThingsPro current release version 2.3

1. Can't dispay Serial Number in Device Enablement Utility.
    Please apply [the updated mxssdpd file](https://www.dropbox.com/s/fot9nmmbzv508aq/mxssdpd?dl=1) to use latest version of ThingsPro Gateway software with the Device Enablement Utility. Copy the file to replace the original one located at `/etc/default/mxssdpd` of the UC-8100 gateway.
