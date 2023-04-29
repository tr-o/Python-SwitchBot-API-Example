# SwitchBot API Python Example

This repository contains a Python example script that demonstrates how to use the SwitchBot API to get the list of devices and their status information, such as temperature, humidity, and battery level.

## Imported Modules

The script imports several Python modules and libraries that are used for various tasks. Here's an explanation of what each module does:

1. \`requests\`: The \`requests\` library is a popular HTTP library for Python. It is used to make API calls to the SwitchBot API to get device information and status. The library simplifies the process of working with HTTP requests and provides methods to send HTTP requests, handle redirection, and process the responses.
2. \`json\`: The \`json\` module is part of Python's standard library and is used to work with JSON data. In this script, it is not directly used since the \`requests\` library can handle JSON data by default. However, if you need to work with JSON data more extensively, this module provides functions like \`json.loads()\` and \`json.dumps()\` for parsing JSON strings and converting Python objects to JSON strings, respectively.
3. \`time\`: The \`time\` module is part of Python's standard library and provides various time-related functions. In this script, it is used to get the current timestamp in milliseconds, which is required for generating the signature for the API header.
4. \`hashlib\`: The \`hashlib\` module is part of Python's standard library and provides various hash algorithms like SHA-256. In this script, it is used to generate the SHA-256 hash for the signature in the API header.
5. \`hmac\`: The \`hmac\` module is part of Python's standard library and provides a way to generate message authentication codes (MAC) using various hash algorithms. In this script, it is used to create a hash-based message authentication code (HMAC) using the SHA-256 algorithm for the signature in the API header.
6. \`base64\`: The \`base64\` module is part of Python's standard library and provides functions to work with Base64 encoding and decoding. In this script, it is used to encode the HMAC signature as a Base64 string.
7. \`uuid\`: The \`uuid\` module is part of Python's standard library and provides functions to generate universally unique identifiers (UUID). In this script, it is used to generate a UUID for the \`nonce\` field in the API header.

## Usage

1. Clone this repository:

\`\`\`bash
git clone https://github.com/yourusername/switchbot-api-python-example.git
\`\`\`

2. Navigate to the cloned repository:

\`\`\`bash
cd switchbot-api-python-example
\`\`\`

3. Open the \`switchbot.py\` file and replace \`<YOUR_API_TOKEN>\` and \`<YOUR_API_SECRET_KEY>\` with your SwitchBot API token and secret key, respectively. You can find these in the SwitchBot app (v6.14 or later).

4. Save the changes and run the script:

\`\`\`bash
python switchbot.py
\`\`\`

The script will fetch the list of devices and display their status information.
