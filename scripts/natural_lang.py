import sys
import pymongo
sys.path.append("../")
from import_config import load_config
from pymongo import MongoClient
import nltk


config = load_config()

client = MongoClient(config["database"]["connection_url"])

db = client[config['database']["database_name"]]

conn = db[config["database"]["collection_name"]]

data = conn.find()


for twitter_object in data:
	twitter_object["process_text"] = nltk.word_tokenize(twitter_object['text'])
	twitter_object["natural_lang"] = nltk.pos_tag(twitter_object["process_text"])
	conn.save(twitter_object)
	




