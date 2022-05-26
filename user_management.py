from locale import currency
from authentication_management import connection
import mysql.connector
from vehicle_management import lookup_car


def add_new_user(first_name, last_name, date_of_birth, email, password, car_reg):
    with connection.cursor(dictionary=True) as cursor:
        try:
            cursor.execute("""INSERT INTO user
                                (first_name, last_name, date_of_birth, email, password)
                                VALUES
                                (%s, %s, %s, %s, %s);""", (first_name, last_name, date_of_birth, email, password))
            connection.commit()
            user_id = cursor.lastrowid
            car_details = lookup_car(car_reg.replace(' ', ''))
            cursor.execute("""INSERT INTO e_vehicle
                              (user_id, make, colour, registrationNumber)
                              VALUES
                              (%s, %s, %s, %s);""", (user_id, car_details['make'], car_details['colour'], car_reg))
            connection.commit()
        except (mysql.connector.IntegrityError, mysql.connector.DataError):
            return {'status': 'failure'}
        else:
            return {'status': 'success'}


def signin_existing_user(email, password):
    with connection.cursor(dictionary=True) as cursor:
        cursor.execute("""SELECT id
                              FROM user
                              WHERE email = %s
                              AND
                              password = %s""", (email, password))
        results = cursor.fetchone()
        return results


def display_user_information(id):
    with connection.cursor(dictionary=True) as cursor:
        cursor.execute("""SELECT CONCAT(first_name, ' ', last_name) AS name, email, date_of_birth
                               FROM user
                               WHERE id = %s;""", (id,))
        results = cursor.fetchone()
        return results


def delete_existing_user(email):
    with connection.cursor(dictionary=True) as cursor:
        cursor.execute("""DELETE FROM user
                              WHERE email = %s""", (email,))
        connection.commit()


# TEST IN PYTHON:

# add_new_user('python', 'm', '2003-03-03', 'python-email@email.com', 'password1234')
# print(add_new_user())

# print(signin_existing_user('ayan-email@email.com', 'password1234'))
# print(check_if_user_exists('ayan-email@email.com', 'password1234'))
# print(display_user_information(1))