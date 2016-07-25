import csv
import pymongo
import sys
import json
sys.path.append("../")
from import_config import load_config
from pymongo import MongoClient

config = load_config()

print(config)

client = MongoClient(config["database"]["connection_url"])

db = client[config["database"]["database_name"]]
conn = db[config["database"]["collection_name"]]



