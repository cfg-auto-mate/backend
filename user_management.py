from authentication_management import connection


def add_new_user(first_name, last_name, date_of_birth, email, password):
    with connection.cursor(dictionary=True) as cursor:
        cursor.execute("""INSERT INTO user
                            (first_name, last_name, date_of_birth, email, password)
                            VALUES
                            (%s, %s, %s, %s, %s);""", (first_name, last_name, date_of_birth, email, password))
        connection.commit()


def signin_existing_user(email, password):
    with connection.cursor(dictionary=True) as cursor:
        cursor.execute("""SELECT id
                              FROM user
                              WHERE email = %s
                              AND
                              password = %s""", (email, password))
        results = cursor.fetchall()
        return results


def display_user_information(id):
    with connection.cursor(dictionary=True) as cursor:
        cursor.execute("""SELECT CONCAT(first_name, ' ', last_name)) AS Name, email, date_of_birth, DATEDIFF(yy,CONVERT(DATE, date_of_birth),GETDATE()) AS AGE
                               FROM user
                               WHERE id = %s;""", (id,))
        results = cursor.fetchall()
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