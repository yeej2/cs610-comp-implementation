import pymongo
from pymongo import MongoClient
import datetime
client = MongoClient()

client = MongoClient('localhost', 27017)

db = client.test_database

collection = db.test_collection
print("test")
post = {
"author": "Mike",
"text": "TEST",
"date": datetime.datetime.utcnow()
}
print("Inserted into collection")
posts = db.posts
print("try1")
post_id = posts.insert_one(post).inserted_id
print("messed up here?")
post_id
print("Definitely here")
print("should be done")
