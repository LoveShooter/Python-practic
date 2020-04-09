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




#my_collection = my_database.foods

#my_collection.insert_one({
#    "_id": 1,
 #   "name": "pizza"
  #  "calories": 266,
   # "fats": {
    #    "saturated": 4.5,
     #   "trans": 0.2
    #},
    #"protein": 11
#})

#my_collection.insert_many([
    #{
    #    "_id": 2,
    #    "name": "hamburger",
    #    "calories": 295, "protein": 17,
    #    "fats": { "saturated": 5.0, "trans": 0.8 },
    #},
    #{
     #   "_id": 3,
      #  "name": "taco",
       # "calories": 226, "protein": 9,
      #  "fats": { "saturated": 4.4, "trans": 0.5 },
   # }
#])




#mydb = myclient['testdb']

#print(mydb)

#print(myclient.list_database_names())

#dblist = myclient.list_database_names()
#if "mydatabase" in dblist:
#   print("The database Exists.")


#response = requests.get('https://jsonplaceholder.typicode.com/users')

#print (response) 
#print (response.status_code)

#for x in response.json():
#    print(x)

#for x in response.json():
#   if x['website'] == 'kale.biz':
#        print(x['name'])
#        print(x['phone'])

