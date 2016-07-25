import csv
import pymongo
import sys
import json
sys.path.append("../")
from import_config import load_config
from pymongo import MongoClient

config = load_config()

client = MongoClient(config["database"]["connection_url"])

db = client[config["database"]["database_name"]]
conn = db[config["database"]["collection_name"]]

data = conn.find()


with open("../tmp/tweets.csv", 'w') as csvfile:
	writer = csv.DictWriter(csvfile, fieldnames=["text"])
	writer.writeheader()
	for document in data:
		sample = {}
		sample["text"] = document["text"]
		writer.writerow(sample)




