from flask import Flask
from flask import jsonify, request
import requests
from flask_cors import CORS
#import sqlite3
import socket
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware

x = socket.gethostbyname(socket.gethostname())
ip_address = {
	"IP Address": x
}

app = Flask(__name__)
CORS(app)
app.config["DEBUG"] = True
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

xray_recorder.configure(service='Front End')
XRayMiddleware(app, xray_recorder)


@app.route('/', methods=['GET'])
def index():
	return "Welcome to Simple Python Microservices"

@app.route('/buku', methods=['GET', 'POST'])
def buku():
	data_buku = requests.get('http://172.17.0.2:5001/buku')
	data_buku.status_code = 200
	print(data_buku)
	return '{} {}'.format(data_buku.json(), x)



@app.route('/film', methods=['GET', 'POST'])
def film():
	data_film = requests.get('http://172.17.0.3:5000/film')
	data_film.status_code = 200
	return '{} {}'.format(data_film.json(), x)


if __name__ == "__main__":
	app.run(host= '0.0.0.0',port='80')