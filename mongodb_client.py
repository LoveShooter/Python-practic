import pymongo

client = pymongo.MongoClient('mongodb+srv://sysadm:Ff121314@cluster0-gpxwq.mongodb.net/')  #Connect to my MongoDB cluster + auth
db = client["testdb"]  #Create DB
mycol = db["test_import_json_collection"]  #Create collection