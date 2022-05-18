"""
INSTALLATION GUIDE
To install flask, run `pip install flask`
To install mysql.connector, run `pip install mysql-connector-python`
"""

from flask import Flask, jsonify, request, session, redirect, render_template, make_response, flash
from datetime import timedelta
from authentication_management import *
from user_management import *
from route_management import *
from vehicle_management import *
from rating_management import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Temporary Secretkey'
app.permanent_session_lifetime = timedelta(days=2)


@app.get('/')
def intro():
    return render_template('base.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup_new_user():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        date_of_birth = request.form.get('date_of_birth')
        email = request.form.get('email')
        password = request.form.get('password')
        signup_user = add_new_user(first_name=first_name, last_name=last_name, date_of_birth=date_of_birth, email=email, password=password)
        return redirect('login')
    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        signin_user = signin_existing_user(email=email, password=password)
        if signin_user is not None:
            session['loggedin'] = True
            session['id'] = signin_user[0]
            session['firstname'] = signin_user[1]
            flash(f"Successful login! Welcome back {session['firstname']}", category='success')
            return redirect('/user')
        else:
            flash("User doesn't exist!", category='error')
    return render_template('login.html')


@app.get('/user')
def get_user_information():
    return render_template('user.html', id=session['id'])


@app.get('/user/<int:id>')
def view_user_information(id):
    user = display_user_information(id)
    return jsonify(user)


@app.get('/route')
def get_route_information():
    if 'loggedin' in session:
        return render_template('route.html', id=session['id'])
    return render_template('login.html')


@app.route('/route', methods=['GET', 'POST'])
def select_new_route():
    if request.method == ['POST']:
        id = request.form.get('id')
        user_id = request.form.get('user_id')
        label = request.form.get('label')
        from_add = request.form.get('from_add')
        to_add = request.form.get('to_add')
        favourite = request.form.get('favourite')
        new_route = create_a_route(id=id, user_id=user_id, label=label, from_add=from_add, to_add=to_add, favourite=favourite)
        flash('Creating your new journey!', category='success')
        return redirect('/route/<search_string>')
    return render_template('signup.html')


@app.get('/route/<int:id>')
def display_selected_route(id):
    route = show_selected_route(id)
    return jsonify(route)


@app.get('/vehicle')
def show_vehicle_info():
    return render_template('vehicle.html')


@app.route('/vehicle', methods=['GET', 'POST'])
def add_new_car():
    if request.method == ['POST']:
        make = request.form.get('make')
        model = request.form.get('model')
        registration = request.form.get('registration')
        add_vehicle = add_new_car(make=make, model=model, registration=registration)
        flash('New car added to your profile!', category='success')
        redirect('vehicle/<int:vehicle_id>')
    return render_template('vehicle.html')


@app.get('/vehicle/<int:id>')
def display_vehicle_info(id):
    vehicle = show_vehicle_info(id)
    return jsonify(vehicle)


@app.get('/rating/<int:id>')
def get_rating_info(id):
    rating = get_ratings(id)
    return jsonify(rating)


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('firstname', None)
    return redirect('/')


app.run(debug=True)
