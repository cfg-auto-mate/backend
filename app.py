"""
INSTALLATION GUIDE
To install flask, run `pip install flask`
To install mysql.connector, run `pip install mysql-connector-python`
"""

from flask import Flask, jsonify, request, redirect, render_template, make_response, flash
from flask_cors import CORS
from authentication_management import *
from user_management_classes import UserDatabase
from route_management_classes import RouteDatabase
from vehicle_management_classes import VehicleDatabase
from rating_management_classes import RatingDatabase

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Temporary Secretkey'
cors = CORS(app)

@app.get('/')
def intro():
    return render_template('base.html')

import requests
@app.get('/test/<lat>/<lng>')
def test(lat, lng):
    response = requests.get(f"https://chargepoints.dft.gov.uk/api/retrieve/registry/lat/{lat}/long/{lng}/dist/10/format/json")
    data = response.json()["ChargeDevice"]
    return jsonify(data)


@app.route('/signup', methods=['GET', 'POST'])
def signup_new_user():
    db = UserDatabase()
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        date_of_birth = request.form.get('date_of_birth')
        email = request.form.get('email')
        password = request.form.get('password')
        signup_user = db.add_new_user(first_name=first_name, last_name=last_name, date_of_birth=date_of_birth, email=email, password=password)
        flash('User created!', category='success')
        return redirect('/')
    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login_user():
    db = UserDatabase()
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        signin_user = db.signin_existing_user(email='email', password='password')
        flash(f"Successful login! Welcome back {email}", category='success')
        return redirect('/user')
    return render_template('login.html')


@app.get('/user')
def get_user_information():
    return redirect('/user/<int:id>')


@app.get('/user/<int:id>')
def view_user_information(id):
    db = UserDatabase()
    user = db.display_user_information(id)
    return jsonify(user)


@app.get('/route')
def get_route_information():
    return render_template('route.html')


@app.route('/route', methods=['GET', 'POST'])
def select_new_route():
    db = RouteDatabase()
    if request.method == ['POST']:
        id = request.form.get('id')
        user_id = request.form.get('user_id')
        label = request.form.get('label')
        from_add = request.form.get('from_add')
        to_add = request.form.get('to_add')
        favourite = request.form.get('favourite')
        new_route = db.create_a_route(id=id, user_id=user_id, label=label, from_add=from_add, to_add=to_add, favourite=favourite)
        flash('Creating your new journey!', category='success')
        return redirect('/route/<search_string>')
    return render_template('signup.html')


@app.get('/route/<search_string>')
def display_selected_route(search_string):
    db = RouteDatabase()
    route = db.show_selected_route(search_string)
    return jsonify(route)


@app.get('/vehicle')
def show_vehicle_info():
    return render_template('vehicle.html')


@app.route('/vehicle', methods=['GET', 'POST'])
def add_new_car():
    db = VehicleDatabase()
    if request.method == ['POST']:
        make = request.form.get('make')
        model = request.form.get('model')
        registration = request.form.get('registration')
        add_vehicle = db.add_new_car(make=make, model=model, registration=registration)
        flash('New car added to your profile!', category='success')
        redirect('vehicle/<int:vehicle_id>')
    return render_template('vehicle.html')


@app.get('/vehicle/<int:id>')
def display_vehicle_info(id):
    db = VehicleDatabase()
    vehicle = db.show_vehicle_info(id)
    return jsonify(vehicle)


@app.get('/rating/<int:id>')
def get_rating_info(id):
    db = RatingDatabase()
    rating = db.get_ratings(id)
    return jsonify(rating)


app.run(debug=True)
