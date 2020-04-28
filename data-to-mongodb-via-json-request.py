import json
import pymongo
import requests
import mongodb_conn_input # Import connection from mongodb_client.py 

from mongodb_conn_input import*
client
db
mycoll

url = requests.get('https://jsonplaceholder.typicode.com/users')
usersinfo = json.loads(url.text)

x = mycoll.insert_many(usersinfo)
