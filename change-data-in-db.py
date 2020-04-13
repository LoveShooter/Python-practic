import json
import mongodb_conn # Import connection from mongodb_conn.py 

from mongodb_conn import* # Import arguments
client
db
mycol

searchquery = {'guest name': 'Max'}

findobject = mycol.find(searchquery)

for x in findobject:
    print(x)