from flask import Flask
from flask import jsonify, request
#import sqlite3
from flask_cors import CORS
import socket

x = socket.gethostbyname(socket.gethostname())

app = Flask(__name__)
CORS(app)
app.config["DEBUG"] = True
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/film', methods=['GET'])
def film():
	film =[
	{
		'Judul':'Avengers',
		'Genre':'Action'
	},
	{
		'Judul':'Spiderman',
		'Genre':'Action'
	},
	{
		"IP Address": x
	}
	]
	response = jsonify(film)
	response.status_code = 200
	return response


if __name__ == "__main__":
	app.run(host= '0.0.0.0',port=5000)