from authentication_management import connection


def add_new_car(user_id, make, model, registration):
    with connection.cursor() as cursor:
        cursor.execute("""INSERT INTO e_vehicle
                          (user_id, make, model, registration)
                          VALUES
                          (%s, %s, %s, %s);""", (user_id, make, model, registration))
        connection.commit()


def show_vehicle_info(id):
    with connection.cursor() as cursor:
        cursor.execute("""SELECT e.make, e.model, e.registration
                              FROM e_vehicle e
                              JOIN user u
                              ON e.user_id = u.id
                              WHERE e.user_id = %s""", (id,))
        results = cursor.fetchall()
        return results


# TEST IN PYTHON:

# add_new_car('1', 'renault', 'zoe', 'NW89 4GB')
# add_new_car('2', 'nissan', 'leaf', 'BT99 0LD')
# add_new_car('3', 'toyota', 'yaris', 'GH77 6FD')
# print(add_new_car())
# print(show_vehicle_info(1))
