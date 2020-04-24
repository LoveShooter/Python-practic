import pymongo


client = pymongo.MongoClient('mongodb+srv://sysadm:Ff121314@cluster0-gpxwq.mongodb.net/')  #Connect to my MongoDB cluster + auth

db = client['to-do-lists']
mycoll = db['todos']

print(db)
print(mycoll)
print("-------------------------------------------")

def insert_data(mycoll, data):
    return mycoll.insert_many(data)

def find_doc(mycoll, elements):
    return mycoll.find_one(elements)

def delete_doc(mycoll, query):
    mycoll.delete_one(query)

owner = input("Enter Owner Name: ")
task = input("Enter Task name: ")
priority = int(input("Choose Priority from 1 to 5: "))

owner2 = input("Enter Owner #2 Name: ")
task2 = input("Enter Task #2 name: ")
priority2 = int(input("Choose Priority from 1 to 5: "))

owner3 = input("Enter Owner #2 Name: ")
task3 = input("Enter Task #2 name: ")
priority3 = int(input("Choose Priority from 1 to 5: "))

to_do_record = [
    {'owner_name': owner, 'task_name': task,'priority': priority},
    {'owner_name': owner2, 'task_name': task2,'priority': priority2},
    {'owner_name': owner3, 'task_name': task3,'priority': priority3},
    ]

print(to_do_record)

print(insert_data(mycoll, to_do_record))

#name = input("Enter Owner Name to search:")
#find_data = {'owner_name': name}
#print(find_data)

find_query = { 'owner_name': input("Enter Owner name to find:") }
print(find_query)
print("---------------------------")

result_find = find_doc(mycoll, find_query)
print(result_find)
print("---------------------------")

query = { 'task_name': input("Enter Task name to delete:") }
print(query)

delete_doc(mycoll, query)

