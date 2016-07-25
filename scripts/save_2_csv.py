import csv
import pymongo
import json
import sys
import json
sys.path.append("../")
from import_config import load_config
from pymongo import MongoClient

config = load_config()

client_bla = MongoClient(config["database"]["connection_url"])

db = client_bla[config["database"]["database_name"]]
conn = db[config["database"]["collection_name"]]

data = conn.find()

with open("../tmp/tweets.csv", 'w') as csvfile:
	writer = csv.DictWriter(csvfile, fieldnames=["text"])
	writer.writeheader()
	for document in data:
		sample = {}
		sample["text"] = document["text"]
		writer.writerow(sample)



>>>>>>> 077fbb27f087894ef76cb095d7cfe5ed3e6353be

