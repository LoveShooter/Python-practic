import pymongo



client = pymongo.MongoClient('mongodb+srv://sysadm:Ff121314@cluster0-gpxwq.mongodb.net/')  #Connect to my MongoDB cluster + auth

mydb = client["myprogdb"]  #Create DB
mycol = mydb["progcollection"]  #Create collection


def insert_data(mycol, data):
    return mycol.insert_one(data).inserted_id

def find_doc(mycol, elements):
    return mycol.find_one(elements)

def delete_doc(mycol, query):
    mycol.delete_one(query)

for record in range(1, 3):
    owner = input("Enter Owner Name: ")
    task = input("Enter Task name: ")
    priority = int(input("Choose Priority from 1 to 5: "))


to_do_record = {
    'owner_name': owner,
    'task_name': task,
    'priority': priority,
    }
    
print(to_do_record)

print(insert_data(mycol, to_do_record))

#name = input("Enter Owner Name to search:")
#find_data = {'owner_name': name}
#print(find_data)

find_query = { 'owner_name': input("Enter Owner name to find:") }
print(find_query)
print("---------------------------")

result_find = find_doc(mycol, find_query)
print(result_find)
print("---------------------------")

query = { 'task_name': input("Enter Task name to delete:") }
print(query)

delete_doc(mycol, query)

