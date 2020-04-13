import pymongo

client = pymongo.MongoClient('mongodb+srv://sysadm:Ff121314@cluster0-gpxwq.mongodb.net/')  #Connect to my MongoDB cluster + auth

inputcol = input("Enter name of collection: ")

db = client["testdb"]  #Create DB
mycol = db["inputcol"]  #Create collection