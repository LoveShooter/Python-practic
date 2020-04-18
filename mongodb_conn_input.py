import pymongo

client = pymongo.MongoClient('mongodb+srv://sysadm:Ff121314@cluster0-gpxwq.mongodb.net/')  #Connect to my MongoDB cluster + auth

inputdb = input("Enter DB name: ")
inputcol = input("Enter name of Collection: ")

db = client["inputdb"]  #Create DB
mycol = db["inputcol"]  #Create collection