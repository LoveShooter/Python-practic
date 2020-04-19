import pymongo
import json
import mongodb_conn_input

from mongodb_conn_input import*
client
db
mycol


def insert_data(mycol, data):
    return mycol.insert_one(data).inserted_id

def find_doc(mycol, elements):
    return mycol.find_one(elements)



#for record in range(1, 3):
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

result = find_doc(mycol, {'owner_name': 'Max'})
print(result)

