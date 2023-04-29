import json
import time
import hashlib
import hmac
import base64
import uuid
import requests

# Function to get device status
def get_device_status(device_id, headers):
    status_url = f"
https://api.switch-bot.com/v1.0/devices/{device_id}/status
"
    status_response = requests.get(status_url, headers=headers)

    if status_response.status_code == 200:
        return status_response.json()
    else:
        print(f"Error retrieving status for device {device_id}: {status_response.status_code} {status_response.text}")
        return None

# Generate API header
apiHeader = {}
# open token
token = '' # copy and paste from the SwitchBot app V6.14 or later
# secret key
secret = '' # copy and paste from the SwitchBot app V6.14 or later
nonce = uuid.uuid4()
t = int(round(time.time() * 1000))
string_to_sign = '{}{}{}'.format(token, t, nonce)

string_to_sign = bytes(string_to_sign, 'utf-8')
secret = bytes(secret, 'utf-8')

sign = base64.b64encode(hmac.new(secret, msg=string_to_sign, digestmod=hashlib.sha256).digest())

apiHeader['Authorization'] = token
apiHeader['Content-Type'] = 'application/json'
apiHeader['charset'] = 'utf8'
apiHeader['t'] = str(t)
apiHeader['sign'] = sign
apiHeader['nonce'] = str(nonce)

# Fetch device list
url = "
https://api.switch-bot.com/v1.0/devices
"
response = requests.get(url, headers=apiHeader)

if response.status_code == 200:
    devices = response.json()
else:
    print("Error:", response.status_code, response.text)
    devices = None

# Process device list and display temperature, humidity, and battery level
if devices:
    device_list = devices['body']['deviceList']

    print("List of Devices:")
    for device in device_list:
        device_id = device['deviceId']
        device_name = device['deviceName']
        print(f"Device ID: {device_id}")
        print(f"Device Name: {device_name}")

        status_data = get_device_status(device_id, apiHeader)

        if status_data and 'body' in status_data:
            temperature = status_data['body'].get('temperature', None)
            humidity = status_data['body'].get('humidity', None)
            battery = status_data['body'].get('battery', None)

            if temperature is not None:
                print(f"Temperature: {temperature}°C")
            else:
                print("Temperature data not available")

            if humidity is not None:
                print(f"Humidity: {humidity}%")
            else:
                print("Humidity data not available")

            if battery is not None:
                print(f"Battery Level: {battery}%")
            else:
                print("Battery level data not available")
        else:
            print("Status data not available")

        print()
