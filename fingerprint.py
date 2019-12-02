# imports
import requests
from urllib3 import disable_warnings

# creds
import creds

# definititions
auth = creds.auth
ip_address = creds.ip_address
mac_address = ''
api_url = 'endpoint/mac-address'

if __name__ == "__main__":

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f'Bearer {auth}'
    }

    payload = {
        'status': 'Known'
    }

    url = f'https://{ip_address}/api/{api_url}/{mac_address}'

    disable_warnings()
    response = requests.patch(url, headers=headers, json=payload, verify=False)

    data = response.json()
    print(data)

