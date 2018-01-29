from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def register():
    pass

@app.route('/track', methods=['POST'])
def track():
    carrier_name = request.form['carrier']
    tracking_id = request.form['trackingid']

    print carrier_name, tracking_id
    
    return render_template('index.html')
@app.route('/submitted', methods=['POST'])
def submitted_form():
    name = request.form['name']
    email = request.form['email']
    site = request.form['site_url']
    comments = request.form['comments']

    return render_template(
        'submitted_form.html',
        name=name,
        email=email,
        site=site,
        comments=comments)
