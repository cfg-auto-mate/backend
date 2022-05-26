from authentication_management import connection
import requests


def add_new_car(user_id, make, model, registration):
    with connection.cursor(dictionary=True) as cursor:
        cursor.execute("""INSERT INTO e_vehicle
                          (user_id, make, colour, fuelType, registrationNumber)
                          VALUES
                          (%s, %s, %s, %s);""", (user_id, make, model, registration))
        connection.commit()


def show_vehicle_info(user_id):
    with connection.cursor(dictionary=True) as cursor:
        cursor.execute("""SELECT e.make, e.colour, e.registrationNumber
                              FROM e_vehicle e
                              JOIN user u
                              ON e.user_id = u.id
                              WHERE e.user_id = %s""", (user_id,))
        results = cursor.fetchone()
        return results


def lookup_car(reg_number):
    url = "https://driver-vehicle-licensing.api.gov.uk/vehicle-enquiry/v1/vehicles"
    payload = '{"registrationNumber": "' + reg_number + '"}'
    headers = {
        'x-api-key': 'WROj3JnkS19XuIs7qWWt99Myxf9WO4NP9EvGIDEL',
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, data=payload)
    return response.json()


# TEST IN PYTHON:

# add_new_car('1', 'renault', 'zoe', 'NW89 4GB')
# add_new_car('2', 'nissan', 'leaf', 'BT99 0LD')
# add_new_car('3', 'toyota', 'yaris', 'GH77 6FD')
# print(add_new_car())
# print(show_vehicle_info(1))
