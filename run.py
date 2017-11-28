#!/usr/bin/env python
from flask import Flask, url_for, render_template, send_from_directory
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
    if "id" in str(r):
        my_json = r.decode('utf8').replace("'", '"')
        my_dict = json.loads(my_json)
        orm.del_lic()
        for dic in my_dict:
            lic = {}
            try:
                lic["applicant"] = dic["applicant"]
                lic["supplier"] = dic["lowestBid"]["supplier"]
                lic["end_date"] = dic["end_date"]
                lic["lowest_bid"] = dic["lowestBid"]["value"]
                lic["start_date"] = dic["start_date"]
                lic["products"] = ""
                product = ""
                for x in range (0,len(dic["products"])):
                    produtos = dic["products"][x]
                    print(produtos["quantity"])
                    product = product + produtos["product_name"] + " "
                    product = product + str(produtos["quantity"]) + "<br>"

                lic["products"] = product
                orm.crt_lic(lic)
            except:
                pass
        return r
    else:
        return orm.get_json_lic()

@app.route('/get_fab', methods=['GET'])
def get_fabricante():
    try:
        r = requests.get('webg4r2.gustavo.roesler.brillinger.vms.ufsc.br:1234/api/open/fabricantes').content
        return r
    except:
            return fb.get_json()

@app.route('/get_forn', methods=['GET'])
def get_fornecedor():
	return orm.get_json_forns()

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
