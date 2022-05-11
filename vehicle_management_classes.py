import mysql.connector


class VehicleDatabase:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Husksql91',
            database='charge_and_go')
        self.cursor = self.connection.cursor(dictionary=True)

    def add_new_car(self, user_id, make, model, registration):
        with self.cursor as connection:
            connection.execute("""INSERT INTO e_vehicle
                              (user_id, make, model, registration)
                              VALUES
                              (%s, %s, %s, %s);""", (user_id, make, model, registration))
            self.connection.commit()

    def show_vehicle_info(self, id):
        with self.cursor as connection:
            connection.execute("""SELECT e.make, e.model, e.registration
                                  FROM e_vehicle e
                                  JOIN user u
                                  ON e.user_id = u.id
                                  WHERE e.user_id = %s""", (id,))
            results = connection.fetchall()
            return results


# TEST FROM PYTHON:
# db= VehicleDatabase()

# db.add_new_car('1', 'renault', 'zoe', 'NW89 4GB')
# db.add_new_car('2', 'nissan', 'leaf', 'BT99 0LD')
# db.add_new_car('3', 'toyota', 'yaris', 'GH77 6FD')

