import pymongo
import requests

myclient = pymongo.MongoClient('mongodb+srv://sysadm:Ff121314@cluster0-gpxwq.mongodb.net/')  #подключаемся к нашему кластеру + аутентифицируемся
mydb = myclient["mydatabase"]  #создаем базу
mycol = mydb["customers"] #добавляем коллекцию в БД


mydict = { "_id": 2, "name": "John", "address": "Highway 37" }  # коллекция (словарь с данными)

x = mycol.insert_one(mydict)   #add mydict(collection) in DB
print(x)

print(mydb.list_collection_names())   #Return a list of all collections in your database

collist = mydb.list_collection_names()    #Check if collection 'customers' exists in DB 
if "customers" in collist:
    print("The collection exists.")


try:                                                                  #с помощью исключений проверяем версию mongodb
    print("MongoDB version os %s" % myclient.server_info()['version'])
except pymongo.errors.OperationFailure as error:
    print(error)
    quit(1)