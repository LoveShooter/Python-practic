import pymongo
import json, bson
from pymongo import MongoClient
from bson import ObjectId


client = pymongo.MongoClient('mongodb+srv://sysadm:Ff121314@cluster0-gpxwq.mongodb.net/')  #Connect to my MongoDB cluster + auth
db = client["userslist"]  #Create DB
mycol = db["users"]  #Create collection 



outputId = []

for el in mycol.find():   
    outputId.append(el['_id'])

print(outputId)



idListEdit = []

for element in mycol.find():
    idListEdit.append(str(element['_id']))

inputId = input("Enter element id:")

if inputId in idListEdit:
    print("ID in collection")
else:
    print("ID not in collection")


#if id in y:
#    id = input("Vvedite id:")
#    y = mycol.find_one({'_id': ObjectId(id)})
#    print(y)
#else:
#    print("Not found")





#print list of the _id values of the inserted documents:
#print(x.inserted_ids)