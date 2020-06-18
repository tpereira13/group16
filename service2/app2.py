import json
import pandas as pd
from flask import Flask, request, Response, flash, jsonify
from waitress import serve


URL = "https://storage.googleapis.com/grupo16/data/trainLabels.csv"

app = Flask(__name__)


@app.route('/cifar-10/random_image/<obj_class>', methods=['POST'])
def random_image(obj_class):
	
	data = {}
	code = 200
	df = pd.read_csv(URL, index_col='id')
	try:
		data['message'] = str(df[df['label'] == obj_class].sample().index[0])
	except:
		data['message'] = 'incorrect class label'
		code = 400 # Bad Request
	finally:
		return Response(response=json.dumps(data), status=code, mimetype="application/json")

if __name__ == "__main__":

    serve(app, host='0.0.0.0', port=8080)