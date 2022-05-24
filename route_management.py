from authentication_management import connection


def create_new_route(user_id, label, from_add, to_add, favourite):
    with connection.cursor(dictionary=True) as cursor:
        cursor.execute("""INSERT INTO route
                          (user_id, label, from_add, to_add, favourite)
                          VALUES
                          (%s, %s, %s, %s, %s);""", (user_id, label, from_add, to_add, favourite))
        connection.commit()


def update_new_route(from_add, to_add, user_id):
    with connection.cursor(dictionary=True) as cursor:
        cursor.execute("""UPDATE route
                          SET from_add = %s, to_add = %s
                          WHERE user_id = %s""", (from_add, to_add, user_id))
        connection.commit()


def show_selected_route(id):
    with connection.cursor(dictionary=True) as cursor:
        cursor.execute("""SELECT r.from_add as START, r.to_add as END, c.name as CHARGING_STOP
                          FROM route r
                          JOIN route_plan_stop p
                          ON r.id = p.route_id
                          JOIN charging_station c
                          ON p.charging_station_id = c.id
                          WHERE r.id = %s;""", (id,))
        results = cursor.fetchall()
        return results


# TEST FROM PYTON:

# create_a_route("7", "1", "road trip", "buckingham palace", "sandringham", "0")
# print(create_ a_route)

# print(show_selected_route(2))