import tweepy
import sys
import pymongo
import json
sys.path.append("../")
from import_config import load_config
from pymongo import MongoClient

config = load_config()
print(config)
client = MongoClient(config["database"]["connection_url"])

db = client[config["database"]["database_name"]]
conn = db[config["database"]["collection_name"]]

auth = tweepy.OAuthHandler(config["twitter"]["consumer_key"], config["twitter"]["consumer_secret"])
auth.set_access_token(config["twitter"]["access_key"], config["twitter"]["access_secret"])
api = tweepy.API(auth)

new_tweets = api.user_timeline(screen_name = "Subtlesnow1", count=200)

for tweet in new_tweets:
	extracted_data = {}
	extracted_data["text"] = tweet.text.encode("utf-8")
	extracted_data["created_at"] = tweet.created_at
	extracted_data["twitter_id"] = tweet.id_str
	conn.insert_one(extracted_data)
	print(extracted_data)












