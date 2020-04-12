import json
import requests
import mongodb_client # Import connection from mongodb_client.py 

from mongodb_client import*
client
db
mycol

r = requests.get('https://jsonplaceholder.typicode.com/users')
usersinfo = json.loads(r.text)

x = mycol.insert_many(usersinfo)

print(usersinfo)