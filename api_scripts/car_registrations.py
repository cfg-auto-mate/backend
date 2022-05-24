# code example

import requests

url = "https://driver-vehicle-licensing.api.gov.uk/vehicle-enquiry/v1/vehicles"

payload = "{\n\t\"registrationNumber\": \"AA19AAA\"\n}"
headers = {
  'x-api-key': 'WROj3JnkS19XuIs7qWWt99Myxf9WO4NP9EvGIDEL',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data = payload)
