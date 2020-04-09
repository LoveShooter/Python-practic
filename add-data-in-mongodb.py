import pymongo
import requests
import datetime



client = pymongo.MongoClient('mongodb+srv://sysadm:Ff121314@cluster0-gpxwq.mongodb.net/')  #Connect to my MongoDB cluster + auth
db = client["testdb"]  #Create DB
collection = db["test-collection"]   #Add collection(create name) in DB



# Create dict with data
post = {"_id": "1",
        "author": "Maxxx",                              
        "text": "My second DB post!",
        "tags": ["mongodb", "python", "python"],
        "date-UTC": datetime.datetime.utcnow()}


#Insert data in DB via insert_one() + print info about id post

post_id = collection.insert_one(post).inserted_id
print(post_id)


