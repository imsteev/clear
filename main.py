from flask import Flask, render_template, request, redirect,url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

from models.Shipment import Shipment
from models.User import User

from services import usps

import json

login_manager = LoginManager()
app = Flask(__name__)
app.config.update(
    DEBUG = True,
    SECRET_KEY = "some secret keyyyyyyyy"
)
login_manager.init_app(app)

# LOOK UP ANCESTOR QUERY
@login_manager.user_loader
def load_user(username):
    return User.query(User.username == username, ancestor=User.ancestor_key).get()

@app.route('/', methods=['GET'])
def index():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
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
    existing_user = User.query(User.username==username).get()

    if existing_user:
        if existing_user.password == password:
            login_user(existing_user)
            return redirect(url_for('index'))
        return render_template('login.html')

    if username and password:
        new_user = User(parent=User.ancestor_key,username=username, password=password)
        login_user(new_user)
        new_user.put()
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@login_manager.unauthorized_handler
def unauthorized():
    # do stuff
    return "You are not authorized or not logged in"
