import mysql.connector


class RatingDatabase:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Husksql91',
            database='charge_and_go')
        self.cursor = self.connection.cursor(dictionary=True)

    # view rating table
    def get_ratings(self, id):
        with self.cursor as connection:
            connection.execute("""SELECT date, score, landmarks, parks, restaurants, shopping, favourite
                                  FROM rating
                                  WHERE user_id = %s;""", (id,))
            results = connection.fetchall()
            return results

    #  add info to rating table
    def add_rating(self, user_id, charging_station_id, date, score, landmarks, parks, restaurants, shopping, favourite):
        # rate a charging station as a user
        with self.cursor as connection:
            connection.execute("""INSERT INTO rating
            (user_id, charging_station_id, date, score, landmarks, parks, restaurants, shopping, favourite)
            VALUES
            (%s, %s, %s, %s, %s, %s, %s, %s, %s);""", (user_id, charging_station_id, date, score, landmarks, parks, restaurants, shopping, favourite))

        connection.commit()



