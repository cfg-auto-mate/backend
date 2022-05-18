#  create decorators to check authentic info input, e.g. correct password, user, email
   # existing user, matching passwords, correct email, length of email, length of password and names

import mysql.connector
from flask import request, redirect
from flask_login import login_user, login_required, logout_user, current_user, LoginManager
from werkzeug.security import generate_password_hash, check_password_hash

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Husksql91',
    database='charge_and_go')



#
# login_manager = LoginManager()
# login_manager.login_view = '/login'
# manage_login = login_manager.init_app(db.display_user_information())
#
#
# @login_manager.user_loader
# def load_user(id):
#     return manage_login.query.get(int(id))
#
# print(load_user(1))


# def check_if_password_is_right(password):
#     hashed_password = generate_password_hash(password, method='sha256')
#     if check_password_hash(hashed_password, password):
#         return True
#     else:
#         return False
#



