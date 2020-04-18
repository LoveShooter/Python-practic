import pymongo
import json
import mongodb_conn_input

from mongodb_conn_input import*
client
db
mycol


def create_record(owner, task, priority):
    "Create record in to do list"
    record = {
        'owner_name': owner,
        'task_name': task,
        'priority': priority,
    }
    print(record)
    return record


def main_record():
    #for tasks in range(1, 5):
    owner = input("Enter Owner Name: ")
    task = input("Enter Task name: ")
    priority = int(input("Choose Priority from 1 to 5: "))
    if priority < 1:
        print ("!Error! You've choosen a number less 1!!!")
    elif priority > 5:
        print ("!Error! You've choosen a number greater than 5!!!")
    create_record(owner, task, priority)

main_record()

to_do_list = mycol.insert_one(main_record())