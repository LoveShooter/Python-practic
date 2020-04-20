import pymongo


newdb = input("Enter DB name:")
newcoll = input("Enter name of Collection:")


client = pymongo.MongoClient('mongodb+srv://sysadm:Ff121314@cluster0-gpxwq.mongodb.net/')  #Connect to my MongoDB cluster + auth


print(newdb)
print(newcoll)

#mydatabase = client.newdb
#mycollection = mydatabase.newcoll

db = client['newdb']  #Create DB
mycol = db['newcoll']  #Create collection


#print(mydatabase)
#print(mycollection)

#mycollection.insert_one({
#    "_id": 1,
#    "name": "pizza",
#    "calories": 266,
#    "fats": {
#        "saturated": 4.5,
#        "trans": 0.2
#    },
#    "protein": 11
#})