import json
import mongodb_client # Import connection from mongodb_client.py 
filename = "Common-currency.json"
#myfile = open(filename, mode='w')


from mongodb_client import* # Import our functions from file
client
db
mycol

# Get the data from JSON file
#open(filename, mode='r')
#json_data = json.load(filename)


#x = mycol.insert_many(filename)



with open('Common_currency.json', 'r') as data_file:
    data_json = json.load(data_file)

#Insert Data
mycol.remove()
mycol.insert(data_json)
