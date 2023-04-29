import requests
import json
import time
import hashlib
import hmac
import base64
import uuid

# Function to get device status
def get_device_status(device_id, headers):
    status_url = f"https://api.switch-bot.com/v1.0/devices/{device_id}/status"
    status_response = requests.get(status_url, headers=headers)

    if status_response.status_code == 200:
        return status_response.json()
    else:
        return None

# Function to set API credentials
def set_api_header(api_token, api_secret_key):
    api_header = {}
    nonce = uuid.uuid4()
    t = int(round(time.time() * 1000))
    string_to_sign = '{}{}{}'.format(api_token, t, nonce)

    string_to_sign = bytes(string_to_sign, 'utf-8')
    secret = bytes(api_secret_key, 'utf-8')

    sign = base64.b64encode(hmac.new(secret, msg=string_to_sign, digestmod=hashlib.sha256).digest())

    api_header['Authorization'] = api_token
    api_header['Content-Type'] = 'application/json'
    api_header['charset'] = 'utf8'
    api_header['t'] = str(t)
    api_header['sign'] = sign
    api_header['nonce'] = str(nonce)

    return api_header

# Function to get device list
def get_device_list(api_header):
    url = "https://api.switch-bot.com/v1.0/devices"
    response = requests.get(url, headers=api_header)

    if response.status_code == 200:
        return response.json()['body']['deviceList']
    else:
        return None

# Function to display device status information
def display_device_status(devices, api_header):
    if devices:
        print("List of Devices:")
        for device in devices:
            device_id = device['deviceId']
            device_name = device['deviceName']
            print(f"Device ID: {device_id}")
            print(f"Device Name: {device_name}")

            status_data = get_device_status(device_id, api_header)

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

# Main function
def main():
    # Set API token and secret key
    api_token = '<YOUR_API_TOKEN>' # copy and paste from the SwitchBot app V6.14 or later
    api_secret_key = '<YOUR_API_SECRET_KEY>' # copy and paste from the SwitchBot app V6.14 or later

    # Set API header with credentials
    api_header = set_api_header(api_token, api_secret_key)

    # Get device list
    devices = get_device_list(api_header)

    # Display device status information
    display_device_status(devices, api_header)

if __name__ == "__main__":
    main()
