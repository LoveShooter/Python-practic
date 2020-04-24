import pymongo


inputdb = input("Enter DB name: ")
coll = input("Enter collection Name: ")
testdataInput = input("Enter testdata: ")
print(inputdb)
print(coll)
print(testdataInput)

input("Press Enter to continue, connect to database")


client = pymongo.MongoClient('mongodb+srv://sysadm:Ff121314@cluster0-gpxwq.mongodb.net/')  #Connect to my MongoDB cluster + auth

db = client[inputdb]

print(db)

mycoll = db[coll]

print(mycoll)

bzhu = {
    'test': testdataInput,
}

insert_result = mycoll.insert_one(bzhu)

input("Ready, press to exit")