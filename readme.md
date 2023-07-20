# MQTT Publisher using MQTT
For standard (non-secure) MQTT connections, use port 1883.
For secure MQTT connections (MQTT over TLS/SSL), use port 8883.
Check the documentation or configuration of the MQTT broker you are connecting to for any custom port numbers they may specify.


test.mosquitto.org

mosquitto_sub.exe -h localhost -t test/tool1