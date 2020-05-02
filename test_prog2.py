import pymongo
import json


client = pymongo.MongoClient('mongodb+srv://sysadm:Ff121314@cluster0-gpxwq.mongodb.net/')  #Connect to my MongoDB cluster + auth

db = client["to-do-lists"]  #Create DB
mycol = db["todos"]  #Create collection
print(db)
print(mycol)

q = {'completed': bool('false')}
q2 = mycol.find(q) # Find by status
print(q2)

