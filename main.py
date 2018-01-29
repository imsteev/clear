from flask import Flask, render_template, request, redirect,url_for
from models.Shipment import Shipment

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', shipments=list(Shipment.query()))

@app.route('/shipments', methods=['GET'])
def shipments():
    return render_template('index.html', shipments=list(Shipment.query()))

@app.route('/track', methods=['POST'])
def track():
    carrier_name = request.form['carrier']
    tracking_id = request.form['trackingid']
    shipment_name = request.form['shipmentname']

    shipment = Shipment(name=shipment_name, carrier=carrier_name, tracking_id=tracking_id)
    shipment.put()
    
    return redirect(url_for('index'))
