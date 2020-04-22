import pymongo

client = pymongo.MongoClient('mongodb+srv://sysadm:Ff121314@cluster0-gpxwq.mongodb.net/')  #Connect to my MongoDB cluster + auth

#mydatabase = client.newdb
#mycollection = mydatabase.newcoll

newdb = str(input("Enter DB name: "))
newcoll = str(input("Enter name of Collection: "))

y = newdb + newcoll

print(y)
print(newdb)
print(newcoll)

mydb = client["newdb"]  #Create DB
mycol = mydb["newcoll"]  #Create collection

print(mydb)
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