import pymongo

inputdb = input("Enter DB name: ")
inputcoll = input("Enter collection Name: ")

print(inputdb)
print(inputcoll)

input("Press Enter to continue, connect to database")

client = pymongo.MongoClient('mongodb+srv://sysadm:Ff121314@cluster0-gpxwq.mongodb.net/')  #Connect to my MongoDB cluster + auth

db = client[inputdb]
mycoll = db[inputcoll]

print(db)
print(mycoll)