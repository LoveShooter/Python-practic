import pymongo

newdb = input('Enter DB name: ' )
newcoll = input('Enter name of Collection: ')

print(newdb)
print(newcoll)

client = pymongo.MongoClient('mongodb+srv://sysadm:Ff121314@cluster0-gpxwq.mongodb.net/')  #Connect to my MongoDB cluster + auth

#mydatabase = client.newdb
#mycollection = mydatabase.newcoll

db = client['newdb']  #Create DB
mycol = db['newcoll']  #Create collection

print(db)
print(mycol)


bzhu = {
    "_id": 1,
    "name": "pizza",
    "calories": 266,
    "fats": {
        "saturated": 4.5,
        "trans": 0.2
    },
    "protein": 11
}

x = mycol.insert_one(bzhu)