Version 1:
![image](https://github.com/kpreforma/mqttWeb/assets/90399563/b68dd9a9-c032-4cdc-99e7-d0f62243fab8)

Version 2:
![image](https://github.com/kpreforma/mqttWeb/assets/90399563/5d001fc3-94dd-4a06-bef5-e5e40f5904f9)


# MQTT Publisher using MQTT

For standard (non-secure) MQTT connections, use port 1883.
For secure MQTT connections (MQTT over TLS/SSL), use port 8883.
Check the documentation or configuration of the MQTT broker you are connecting to for any custom port numbers they may specify.

# Create py environment

py -3 -m venv .venv
.venv\Scripts\activate
pip install Flask

# To run Flask app

py main.py

