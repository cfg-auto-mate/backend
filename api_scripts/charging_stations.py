#  file handling: pull api info into json format
#  select key:values of the info to be pulled
#  export selected info into database or own file
# api url: http://chargepoints.dft.gov.uk/api/retrieve/registry/postcode/{POSTCODE}/dist/10/limit/10/format/json
import csv

import requests
import pprint
# import geocoder

# All the charging station within a 10 mile radius of your position(lat+lon)
# http://chargepoints.dft.gov.uk/api/retrieve/registry/lat/51.545581/long/-0.077301/dist/10/

# g = geocoder.ip('me')
# print(g.lat)
# request = requests.get(f"http://chargepoints.dft.gov.uk/api/retrieve/registry/lat/{g.lat}/long/{g.lng}/dist/10")
# response = request.json()
# pprint.pp(response)

# all charging stations based on postcode:
request = input(str("Enter your postcode: "))
post_code = request.replace(" ", "+")
print(post_code)

response = requests.get(
    f"http://chargepoints.dft.gov.uk/api/retrieve/registry/postcode/{post_code}/dist/10/limit/10/format/json")
charging_station_data = response.json()


# pprint.pp(charging_station_data)
# pprint.pp(charging_station_data.json().keys())

# PRINT OUT LIST OF CHARGING STATION IDs:
# LIST COMPREHENSION:
def charging_station_ids():
    device_id_list = [charging_station_id['ChargeDeviceId'] for charging_station_id in charging_station_data['ChargeDevice']]
    return device_id_list
#
# #
# # print(charging_station_ids())
#
#
def charging_station_names():
    device_names_list = [charging_station_name['ChargeDeviceName'] for charging_station_name in charging_station_data['ChargeDevice']]
    return device_names_list
#
#
# # print(charging_station_names())

# OR FOR LOOP:
def charging_station_ids():
      for charging_station_id in charging_station_data['ChargeDevice']:
        print(charging_station_id['ChargeDeviceId'])


charging_station_ids()

def charging_station_names():
    for charging_station_name in charging_station_data['ChargeDevice']:
        print(charging_station_name['ChargeDeviceName'])

charging_station_names()


#
# insert found charging stations to a file:
# with open("charging_devices.csv", "w+") as charging_devices:
#     for device_id in device_id_list:
#         charging_devices.write(f"Charging Station ID: ")

# device_id = [device_id['ChargeDeviceId'] for device_id in response['ChargeDevice']]
# print(device_id)
# print(f"This is the first device id: {device_id[0]}
