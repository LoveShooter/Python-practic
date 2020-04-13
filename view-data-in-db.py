import json
import mongodb_conn # Import connection from mongodb_conn.py 

from mongodb_conn import* # Import arguments
client
db
mycol

x = mycol.find_one()    # Show first object in collection
print(x)                


print("----------------------------------------------------------")


for x in mycol.find():  # Show all objects in collection
    print(x)



