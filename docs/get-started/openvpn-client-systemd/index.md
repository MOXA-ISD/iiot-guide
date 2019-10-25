# Setup OpenVPN Client on Device

1. Install OpenVPN

    ```
    $ sudo apt-get install openvpn
    ```

2. Check the current settings of OpenVPN client service

    ```
    $ systemctl cat openvpn-client@test
    ```

    ![CurrentSettings.png](./images/1.png)

3. Override OpenVPN service with our own settings

    ```
    $ systemctl edit openvpn-client@test
    ```

    ![Override.png](./images/2.png)

4. Check the OpenVPN service again and make sure the override settings appears 

    ```
    $ systemctl cat openvpn-client@test
    ```

    ![OverrideSettings.png](./images/3.png)

5. Enable the OpenVPN service to run while booting

    ```
    $ systemctl enable openvpn-client@test
    ```

    ![Enable.png](./images/4.png)