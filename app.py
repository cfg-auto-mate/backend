from flask import Flask, jsonify, request, session
import requests
from flask_cors import CORS
from authentication_management import *
from user_management import *
from route_management import *
from vehicle_management import *
from rating_management import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Temporary Secretkey'
CORS(app)


@app.get('/charging-stations/<lat>/<lng>')
def charging_stations(lat, lng):
    response = requests.get(f"https://chargepoints.dft.gov.uk/api/retrieve/registry/lat/{lat}/long/{lng}/dist/10/format/json")
    data = response.json()["ChargeDevice"]
    return jsonify(data)


@app.post('/signup')
def signup_new_user():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    date_of_birth = request.form.get('date_of_birth')
    email = request.form.get('email')
    password = request.form.get('password')
    car_reg = request.form.get('car_reg')
    signup_user = add_new_user(first_name=first_name, last_name=last_name, date_of_birth=date_of_birth, email=email, password=password, car_reg=car_reg)
    return jsonify(signup_user)


@app.post('/login')
def login_user():
    email = request.form.get('email')
    password = request.form.get('password')
    signin_user = signin_existing_user(email=email, password=password)
    return jsonify(signin_user)


@app.get('/user/<int:id>')
def view_user_information(id):
    user = display_user_information(id)
    vehicle = show_vehicle_info(id)
    return jsonify({"user": user, "vehicle": vehicle})


@app.post('/route')
def select_new_route():
    id = request.form.get('id')
    user_id = request.form.get('user_id')
    label = request.form.get('label')
    from_add = request.form.get('from_add')
    to_add = request.form.get('to_add')
    favourite = request.form.get('favourite')
    new_route = create_new_route(id=id, user_id=user_id, label=label, from_add=from_add, to_add=to_add, favourite=favourite)
    return jsonify(new_route)


@app.get('/route/<int:id>')
def display_selected_route(id):
    route = show_selected_route(id)
    return jsonify(route)


@app.get('/rating/<int:id>')
def get_rating_info(id):
    rating = get_ratings(id)
    return jsonify(rating)


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('firstname', None)
    return session.pop


app.run(debug=True, port=4000)
