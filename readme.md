# MQTT Publisher using MQTT

For standard (non-secure) MQTT connections, use port 1883.
For secure MQTT connections (MQTT over TLS/SSL), use port 8883.
Check the documentation or configuration of the MQTT broker you are connecting to for any custom port numbers they may specify.

# Create py environment

py -3 -m venv .venv
.venv\Scripts\activate
pip install Flask

# To run Flask app

flask --app hello run

# To create React app

npx create-react-app reactflaskweb

# Add proxy in packagelock

"proxy": "http://localhost:5000/",
