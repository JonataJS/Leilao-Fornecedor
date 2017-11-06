#!/usr/bin/env python
from flask import Flask, url_for, render_template, send_from_directory, jsonify, request
import jinja2.exceptions
import os
from model.fake_lic import *
from model.fake_fab import *
from db.orm import *
import requests

app = Flask(__name__)
fb = Fake_Fab()
orm = Orm()

@app.route('/')
def index():
    return render_template('login.html')


@app.route('/get_lic', methods=['GET'])
def get_license():
    r = requests.get('http://athena-ine5646.herokuapp.com/api').content
    return r

@app.route('/get_fab', methods=['GET'])
def get_fabricante():
    return fb.get_json()


#TODO post forn
@app.route('/get_forn', methods=['GET'])
def get_fornecedor():
	return orm.get_json_forns()

@app.route('/send_bid', methods=['POST'])
def send_lance():
    lance = dict(request.get_json(force=False))
    lance["bidding"] = int(lance["bidding"])
    lance["value"] = int(lance["value"])
    print(lance)
    lance = json.dumps(lance)
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    response = requests.post("https://athena-ine5646.herokuapp.com/api/bids", data=lance, headers=headers)
    print(response)
    return str(response)

@app.route('/<pagename>')
def admin(pagename):
    return render_template(pagename+'.html')

@app.route('/<path:resource>')
def serveStaticResource(resource):
	return send_from_directory('static/', resource)

@app.errorhandler(404)
def not_found(e):
    return '<strong>Page Not Found!</strong>', 404

if __name__ == '__main__':
    try:
        port = int(os.environ.get("PORT", 5000))
        app.run(host='0.0.0.0', port=port, debug=True)
    except KeyboardInterrupt:
        raise SystemExit
