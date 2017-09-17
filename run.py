#!/usr/bin/env python
from flask import Flask, url_for, render_template, send_from_directory
import jinja2.exceptions
from model.fake_lic import *
from model.fake_fab import *


app = Flask(__name__)
fl = Fake_Lic()
fb = Fake_Fab()

@app.route('/')
def index():
    return render_template('login.html')


@app.route('/get_lic', methods=['GET'])
def get_license():
    return fl.get_json()

@app.route('/get_fab', methods=['GET'])
def get_fabricante():
    return fb.get_json()

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
    app.run(host="localhost", port=5000 ,debug=True)
