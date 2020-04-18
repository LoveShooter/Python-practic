import pymongo
import requests
#import mongodb_conn_input

x = int(input("Vvedite a: "))
y = int(input("Vvedite b: "))


def summa(x, y):
    return x + y

z = summa(x, y)
print(z)

def newfunc(n):
    def myfunc(x):
        return x + n
    return myfunc


#owner = input("Enter Owner name: ")
#task = input("Enter Task name: ")
#priority = input("Input Priority of Task from 1 to 5: ")

#p#rint(owner)
#print(task)
#print(priority)

def create_record(owner, task, priority):
    "Create record in to do list"
    record = {
        'owner_name': owner,
        'task_name': task,
        'priority': priority,

    }
    return record


owner = input("Enter Owner name: ")
task = input("Enter Task name: ")
priority = input("Input Priority of Task from 1 to 5: ")

print (create_record(owner, task, priority))

