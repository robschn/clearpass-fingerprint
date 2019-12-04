# imports
import requests

# creds
import creds

# definititions
auth = creds.auth
ip_address = creds.ip_address
mac_address = 'f82d7cbc607c'
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

    response = requests.get(url, headers=headers, json=payload)

    data = response.json()
    print(data)

