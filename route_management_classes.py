import mysql.connector


class RouteDatabase:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Husksql91',
            database='charge_and_go')
        self.cursor = self.connection.cursor(dictionary=True)

    def create_a_route(self, id, user_id, label, from_add, to_add, favourite):
        with self.cursor as connection:
            connection.execute("""INSERT INTO route
                                  (id, user_id, label, from_add, to_add, favourite)
                                  VALUES
                                  (%s, %s, %s, %s, %s, %s);""", (id, user_id, label, from_add, to_add, favourite))
            self.connection.commit()

    def show_selected_route(self, id):
        with self.cursor as connection:
            connection.execute("""SELECT r.from_add as START, r.to_add as END, c.name as CHARGING_STOP
                              FROM route r
                              JOIN route_plan_stop p
                              ON r.id = p.route_id
                              JOIN charging_station c
                              ON p.charging_station_id = c.id
                              WHERE r.id = %s;""", (id,))
            results = connection.fetchall()
            return results


# TEST FROM PYTON:

# db = RouteDatabase()
# new_route = db.select_a_route("7", "1", "road trip", "buckingham palace", "sandringham", "0")
# print(new_route)

# print(db.show_selected_route(2))