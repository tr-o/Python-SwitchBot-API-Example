# Python-SwitchBot-API-Example
This Python script demonstrates how to use the SwitchBot API to retrieve the status of SwitchBot devices and display the temperature, humidity, and battery level for each device.

# Prerequisites
Before running this script, you will need:

A SwitchBot account and devices that you want to monitor.
The latest version of the SwitchBot app installed on your mobile device.
Python 3.x installed on your computer.
The following Python modules installed: requests, json, time, hashlib, hmac, base64, uuid.

# Installation and Usage
Clone or download this repository to your local machine.

Open a terminal or command prompt and navigate to the directory where the script is located.

Install the required Python modules if they are not already installed. For example, you can use pip to install the requests module by running the following command:

Copy code
pip install requests
Open the script file switchbot_api.py in a text editor.

Copy and paste your SwitchBot API token and secret key from the SwitchBot app into the script, replacing the empty strings token and secret:

Copy code
token = '<YOUR_API_TOKEN>'
secret = '<YOUR_API_SECRET>'
Save the script file.

Run the script by executing the following command in the terminal:

Copy code
python switchbot_api.py
The script will fetch a list of your SwitchBot devices and display the temperature, humidity, and battery level for each device.

# License
This script is released under the MIT License. See the LICENSE file for details.

# Credits
This script was written by [Your Name] and is based on the SwitchBot API documentation.
