from flask import Flask, render_template, request, redirect,url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

from models.Shipment import Shipment
from models.User import User

login_manager = LoginManager()
app = Flask(__name__)
app.secret_key = "some secret key tf"
login_manager.init_app(app)

@login_manager.user_loader
def load_user(username):
    return User.query(User.username == username).get()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shipments', methods=['GET'])
@login_required
def shipments():
    return render_template('shipments.html', shipments=list(Shipment.query()))

@app.route('/track', methods=['POST'])
@login_required
def track():
    carrier_name = request.form['carrier']
    tracking_id = request.form['trackingid']
    shipment_name = request.form['shipmentname']

    shipment = Shipment(name=shipment_name, carrier=carrier_name, tracking_id=tracking_id)
    shipment.put()
    
    return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    username = request.form['username']
    password = request.form['password']
    existing_user = User.query(User.username==username and User.password==password).get()

    if existing_user:
        login_user(existing_user)
        print('Logged in successfully.')

        return redirect(url_for('index'))
    elif username and password:
        new_user = User(username=username, password=password)
        new_user.put()
        login_user(new_user)
        print('Registered and logged in successfully')
        return redirect(url_for('index'))

    print('unable to login')
    return render_template('login.html')

@app.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@login_manager.unauthorized_handler
def unauthorized():
    # do stuff
    return "You are not authorized"
