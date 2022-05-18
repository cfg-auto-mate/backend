from authentication_management import connection


# view rating table
def get_ratings(id):
    with connection.cursor() as cursor:
        cursor.execute("""SELECT date, score, landmarks, parks, restaurants, shopping, favourite
                              FROM rating
                              WHERE user_id = %s;""", (id,))
        results = cursor.fetchall()
        return results


#  add info to rating table
def add_rating(user_id, charging_station_id, date, score, landmarks, parks, restaurants, shopping, favourite):
    # rate a charging station as a user
    with connection.cursor() as cursor:
        cursor.execute("""INSERT INTO rating
                          (user_id, charging_station_id, date, score, landmarks, parks, restaurants, shopping, favourite)
                          VALUES
                          (%s, %s, %s, %s, %s, %s, %s, %s, %s);""", (user_id, charging_station_id, date, score, landmarks, parks, restaurants, shopping, favourite))

        connection.commit()


# delete rating:
def remove_favourite(charging_station_id):
    with connection.cursor() as cursor:
        cursor.execute("""DELETE FROM rating
                              WHERE favourites = %s""", (charging_station_id,))
        connection.commit()
