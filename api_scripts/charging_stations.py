import requests

import pprint
# import geocoder
from flask import jsonify

# api url for POST CODE: http://chargepoints.dft.gov.uk/api/retrieve/registry/postcode/{POSTCODE}/dist/10/limit/10/format/json
# api url for LONG&LAT: http://chargepoints.dft.gov.uk/api/retrieve/registry/lat/{g.lat}/long/{g.lng}/dist/10/format/json

# All the charging station within a 10 mile radius of your position(lat+lon)
# http://chargepoints.dft.gov.uk/api/retrieve/registry/lat/51.545581/long/-0.077301/dist/10/

# request = requests.get(f"http://chargepoints.dft.gov.uk/api/retrieve/registry/lat/{g.lat}/long/{g.lng}/dist/10")
# response = request.json()
# pprint.pp(response)

# all charging stations based on postcode:
# request = input(str("Enter your postcode: "))
# post_code = request.replace(" ", "+")
# print(post_code)
#
# response = requests.get(f"http://chargepoints.dft.gov.uk/api/retrieve/registry/postcode/{post_code}/dist/10/limit/10/format/json")
# charging_station_data = response.json()

# pprint.pp(charging_station_data)
# pprint.pp(charging_station_data.json().keys())


# To find lat & long:
# def charging_station_lat_long():
#     lat_long = []
#     for charging_station_lat in charging_station_data['ChargeDevice']:
#         lat_long.append(charging_station_lat['ChargeDeviceLocation']['Latitude'])
#     for charging_station_long in charging_station_data['ChargeDevice']:
#         lat_long.append(charging_station_long['ChargeDeviceLocation']['Longitude'])
#     return lat_long
#
# print(charging_station_lat_long())

def charging_stations():
    response = requests.get(f"https://chargepoints.dft.gov.uk/api/retrieve/registry/lat/51.49399/long/-0.01045/dist/10/format/json")
    data = response.json()["ChargeDevice"]['ChargeDeviceName']
    return jsonify(data)


print(charging_stations())

# def charging_station_names():
#     for charging_station_name in charging_station_data['ChargeDevice']:
#         print(charging_station_name['ChargeDeviceName'])
#
# charging_station_names()


# PRINT OUT LIST OF CHARGING STATION IDs:
# LIST COMPREHENSION:
# def charging_station_ids():
#     device_id_list = [charging_station_id['ChargeDeviceId'] for charging_station_id in charging_station_data['ChargeDevice']]
#     return device_id_list
#
#
# def charging_station_names():
#     device_names_list = [charging_station_name['ChargeDeviceName'] for charging_station_name in charging_station_data['ChargeDevice']]
#     return device_names_list
#
#
# # print(charging_station_names())

# OR FOR LOOP:
# def charging_station_ids():
#       for charging_station_id in charging_station_data['ChargeDevice']:
#         print(charging_station_id['ChargeDeviceId'])
#
#
# charging_station_ids()
#
# def charging_station_names():
#     for charging_station_name in charging_station_data['ChargeDevice']:
#         print(charging_station_name['ChargeDeviceName'])
#
# charging_station_names()

