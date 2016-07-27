import csv
import pymongo
import sys
sys.path.append("../")
from import_config import load_config
from pymongo import MongoClient
from flask import Flask, jsonify, make_response


config = load_config()

client = MongoClient(config["database"]["connection_url"])

db = client[config['database']["database_name"]]

conn = db[config["database"]["collection_name"]]

data = conn.find()

app = Flask(__name__)

@app.route('/')
def index():
	response = []
	for tweet in data:
		modified = {}
		modified["natural_lang"] = tweet["natural_lang"]
		response.append(modified)


	return make_response(jsonify({"tweets": response}), 200)

if __name__ == '__main__':
    app.run(debug=True)