# SwitchBot API Python Example

This repository contains a Python example script that demonstrates how to use the SwitchBot API to get the list of devices and their status information, such as temperature, humidity, and battery level.

## Features

1. **Fetch Device List**: The script uses the SwitchBot API to retrieve a list of devices connected to your SwitchBot account. It displays the device ID and name for each device in the list.

2. **Display Device Status**: For each device, the script fetches and displays the status information, including temperature, humidity, and battery level (if available).

3. **Secure API Authentication**: The script generates a secure signature for API requests using the HMAC-SHA256 algorithm, ensuring that your API credentials remain safe.

4. **Error Handling**: The code includes error handling to manage unsuccessful API responses or missing data, ensuring that the script does not crash and provides meaningful messages to the user.

5. **Easy Setup**: The script only requires the `requests` library, which is a popular Python library for making HTTP requests. Other dependencies are part of Python's standard library, making it simple to set up and run the script on most systems.

6. **Cross-platform Compatibility**: The code is written in Python, a widely used and platform-independent programming language, allowing the script to run on various operating systems, such as Windows, macOS, and Linux, with Python and the required libraries installed.


## Usage

1. Clone this repository:

```bash
git clone https://github.com/yourusername/switchbot-api-python-example.git
```

2. Navigate to the cloned repository:

```bash
cd switchbot-api-python-example
```

3. Open the `switchbot.py` file and replace `<YOUR_API_TOKEN>` and `<YOUR_API_SECRET_KEY>` with your SwitchBot API token and secret key, respectively. You can find these in the SwitchBot app (v6.14 or later).

4. Save the changes and run the script:

```bash
python switchbot.py
```

The script will fetch the list of devices and display their status information.

## Script Overview

The script contains the following functions:

1. `set_api_header(api_token, api_secret_key)`: Sets the API credentials and returns a dictionary containing the headers required for API requests.
2. `get_device_list(api_header)`: Retrieves a list of devices and their basic information.
3. `get_device_status(device_id, headers)`: Retrieves the status information for a specific device.
4. `display_device_status(devices, api_header)`: Displays the list of devices and their status information.
5. `main()`: The main function that calls the other functions and executes the script.

To use the script, simply follow the usage instructions provided in this README.


## Imported Modules

The script imports several Python modules and libraries that are used for various tasks. Here's an explanation of what each module does:

1. `requests`: The `requests` library is a popular HTTP library for Python. It is used to make API calls to the SwitchBot API to get device information and status. The library simplifies the process of working with HTTP requests and provides methods to send HTTP requests, handle redirection, and process the responses.
2. `json`: The `json` module is part of Python's standard library and is used to work with JSON data. In this script, it is not directly used since the `requests` library can handle JSON data by default. However, if you need to work with JSON data more extensively, this module provides functions like `json.loads()` and `json.dumps()` for parsing JSON strings and converting Python objects to JSON strings, respectively.
3. `time`: The `time` module is part of Python's standard library and provides various time-related functions. In this script, it is used to get the current timestamp in milliseconds, which is required for generating the signature for the API header.
4. `hashlib`: The `hashlib` module is part of Python's standard library and provides various hash algorithms like SHA-256. In this script, it is used to generate the SHA-256 hash for the signature in the API header.
5. `hmac`: The `hmac` module is part of Python's standard library and provides a way to generate message authentication codes (MAC) using various hash algorithms. In this script, it is used to create a hash-based message authentication code (HMAC) using the SHA-256 algorithm for the signature in the API header.
6. `base64`: The `base64` module is part of Python's standard library and provides functions to work with Base64 encoding and decoding. In this script, it is used to encode the HMAC signature as a Base64 string.
7. `uuid`: The `uuid` module is part of Python's standard library and provides functions to generate universally unique identifiers (UUID). In this script, it is used to generate a UUID for the `nonce` field in the API header.


## Code Evaluation

1. **Functionality**: The code serves its purpose by using the SwitchBot API to fetch a list of devices and display their status information, such as temperature, humidity, and battery level. It uses functions to modularize the code and make it easier to understand and maintain.

2. **Code structure**: The code is organized into functions, which makes it modular and easy to follow. Each function has a specific responsibility, and the main function calls the other functions to execute the script. This approach makes the code more maintainable and easier to understand.

3. **Readability**: The code is written in a clear and easy-to-understand manner, with descriptive variable and function names. It also includes comments to explain the purpose of each function, which improves the readability of the code.

4. **Error handling**: The code checks for potential issues, such as unsuccessful API responses, and handles them gracefully by returning `None` or displaying appropriate messages. This ensures that the script does not crash or display incorrect information when encountering errors.

5. **Security**: The code uses the HMAC-SHA256 algorithm to generate the signature for the API header, which is a secure and widely used method for API authentication. However, the API token and secret key are hardcoded in the script, which is not recommended for production environments. It would be better to use environment variables or a configuration file to store these sensitive credentials.

6. **Dependencies**: The code relies on the `requests` library, which is a popular and widely used library for making HTTP requests in Python. The other imported modules are part of Python's standard library and do not require any additional installation. This makes the script easy to set up and run on most systems.

7. **Portability**: The code is written in Python, which is a widely used and platform-independent programming language. This means that the script can be run on various operating systems, such as Windows, macOS, and Linux, as long as Python and the required libraries are installed.
