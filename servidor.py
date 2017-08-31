from flask import Flask, url_for, render_template, send_from_directory, jsonify, request
from flask_cors import CORS, cross_origin
import jinja2.exceptions


app = Flask(__name__, static_folder="web/static", template_folder="web/templates")
CORS(app)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/home')
def login():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="localhost", port=5000 ,debug=True)
