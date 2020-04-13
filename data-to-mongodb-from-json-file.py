import json
import mongodb_conn_input # Import connection from mongodb_client.py 
filename = "posts.json"
#myfile = open(filename, mode='w')


from mongodb_conn_input import* # Import our functions from file
client
db
mycol

# Get the data from JSON file
#open(filename, mode='r')
#json_data = json.load(filename)


#x = mycol.insert_many(filename)

with open('G:\OneDrive\coding\python\Lessons\Python-practic\posts.json') as f:
    data_from_json = json.load(f)

#Insert Data
x = mycol.insert_one(f)
print(x)
