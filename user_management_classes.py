import mysql.connector


class UserDatabase:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Husksql91',
            database='charge_and_go')
        self.cursor = self.connection.cursor(dictionary=True)

    def add_new_user(self, first_name, last_name, date_of_birth, email, password):
        with self.cursor as connection:
            connection.execute("""INSERT INTO user
                                (first_name, last_name, date_of_birth, email, password)
                                VALUES
                                (%s, %s, %s, %s, %s);""", (first_name, last_name, date_of_birth, email, password))
            self.connection.commit()

    def signin_existing_user(self, email, password):
        with self.cursor as connection:
            connection.execute("""SELECT email, password
                                  FROM user
                                  WHERE email = %s
                                  AND
                                  password = %s""", (email, password))
            results = connection.fetchall()
            if results is not None:
                return results

    def display_user_information(self, id):
        with self.cursor as connection:
            connection.execute("""SELECT first_name, last_name, date_of_birth, email
                                   FROM user
                                   WHERE id = %s;""", (id,))
            results = connection.fetchall()
            if results is not None:
                return results[0]

    # def check_if_user_exists(self, id):  #use the flask_login module instead for user authentication?

    # def delete_existing_user(self, email):
    #     with self.cursor as connection:
    #         connection.execute("""DELETE FROM user
    #                               WHERE email = %s""", (email,))
    #         connection.commit()


# TEST FROM PYTHON:

# db = UserDatabase()
# new_user = db.add_new_user('ioana', 'm', '2003-03-03', 'ioana-email@email.com', 'password1234')
# print(new_user)

# user_info = db.display_user_information(1)
# print(user_info)