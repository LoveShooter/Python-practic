import json
import mongodb_conn # Import connection from mongodb_conn.py 

from mongodb_conn import* # Import arguments
client
db
mycol

#Find value in collection 'guest_name': 'Alena'
search_query = {'guest_name': 'Alena'}
findobject = mycol.find(search_query)   

for x in findobject:
    print(x)

print("----------------------------------------------")

#Change value 'guest_name': 'Alena'
newvalues = {'$set': {'guest_name': 'JAMES BOND'}}

y = mycol.update_one(search_query, newvalues)



#Print all data after update
for y in mycol.find():
    print(y)

print("----------------------------------------------")


#Delete data with value 'guest_name': Max

delete_query = {'guest_name': 'Max'}

x = mycol.delete_many(delete_query)
print(x.deleted_count, "lines deleted")