from authentication_management import connection


def add_new_user(first_name, last_name, date_of_birth, email, password):
    with connection.cursor() as cursor:
        cursor.execute("""INSERT INTO user
                            (first_name, last_name, date_of_birth, email, password)
                            VALUES
                            (%s, %s, %s, %s, %s);""", (first_name, last_name, date_of_birth, email, password))
        connection.commit()


# check if user exists to create session based on user id
# use the flask_login module instead for user authentication?
def check_if_user_exists(email, password):
    with connection.cursor() as cursor:
        cursor.execute("""SELECT *
                              FROM user
                              WHERE email = %s
                              AND
                              password = %s""", (email, password))
        results = cursor.fetchone()
        return results


def signin_existing_user(email, password):
    with connection.cursor() as cursor:
        cursor.execute("""SELECT *
                              FROM user
                              WHERE email = %s
                              AND
                              password = %s""", (email, password))
        results = cursor.fetchone()
        return results


def display_user_information(id):
    with connection.cursor() as cursor:
        cursor.execute("""SELECT first_name, last_name, date_of_birth, email
                               FROM user
                               WHERE id = %s;""", (id,))
        results = cursor.fetchall()
        if results is not None:
            return results[0]


def delete_existing_user(email):
    with connection.cursor() as cursor:
        cursor.execute("""DELETE FROM user
                              WHERE email = %s""", (email,))
        connection.commit()


# TEST IN PYTHON:

# add_new_user('python', 'm', '2003-03-03', 'python-email@email.com', 'password1234')
# print(add_new_user())

# print(check_if_user_exists('ayan-email@email.com', 'password1234'))
# print(display_user_information(1)