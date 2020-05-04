import pymongo
import requests
import json, bson
import random
import datetime
import os
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_cors import CORS



class JSONEncoder(json.JSONEncoder):                           
    ''' extend json-encoder class'''    
    def default(self, o):                               
        if isinstance(o, ObjectId):
            return str(o)                               
        if isinstance(o, datetime.datetime):
            return str(o)
        return json.JSONEncoder.default(self, o)

app = Flask(__name__)
CORS(app)   # This will enable CORS for all routes


app.config['MONGO_DBNAME'] = 'userslist' # Name of database on mongo
app.config["MONGO_URI"] = "mongodb+srv://sysadm:Ff121314@cluster0-gpxwq.mongodb.net/userslist" #URI to Atlas cluster  + Auth Credentials

mongo = PyMongo(app)

# use the modified encoder class to handle ObjectId & datetime object while jsonifying the response.
app.json_encoder = JSONEncoder

@app.route('/', methods=['GET']) # Hello message
def index():
    
    return 'Hello! It works!'



@app.route('/get_data', methods=['GET'])  # Find all data in my collection
def get_all_data():
    user = mongo.db.users # Connect to my collection

    output = []

    for q in user.find():   # q - like query
        output.append({'id': q['id'], 'name': q['name'], 'username': q['username'], 'email': q['email'], 'address': q['address'], 'phone': q['phone'], 'website': q['website'], 'company': q['company']})

    return jsonify({'result': output})


@app.route('/add_data', methods=['POST']) # Add data in db. Need input JSON-like data.
def add_data():
    user = mongo.db.users
    
    _id = request.json['id']
    _name = request.json['name']
    _username = request.json['username']
    _email = request.json['email']
    _phone = request.json['phone']
    _website = request.json['website']

    user_id = user.insert({'id': _id, 'name': _name, 'username': _username, 'email': _email, 'phone': _phone, 'website': _website})
    new_user = user.find_one({'_id': user_id})

    output = {'id': new_user['id'], 'name': new_user['name'], 'username': new_user['username'], 'email': new_user['email'], 'phone': new_user['phone'], 'website': new_user['website']}

    return jsonify({'result': output})


@app.route('/del_data/<int:user_id>', methods=['GET'])  # Delete data by user ID
def del_one_data(user_id):
    usercoll = mongo.db.users
    delete_user = usercoll.delete_one({'id': int(user_id)}) 
    
    resp = jsonify('Task deleted successfully!')
    resp.status_code = 200
	
    return resp


@app.route('/add_data_placeholder', methods=['GET'])  # Send a request to the API and add data in mongodb from jsonplaceholder
def add_data_placeholder():
    mycoll = mongo.db.users
    
    url1 = 'https://jsonplaceholder.typicode.com/users/6'
    url2 = 'https://jsonplaceholder.typicode.com/users/5'
    url3 = 'https://jsonplaceholder.typicode.com/users/8'
    url4 = 'https://jsonplaceholder.typicode.com/users/10'
    url5 = 'https://jsonplaceholder.typicode.com/users/4'
    
    urls = [url1, url2, url3, url4, url5]

    url = requests.get(random.choice(urls))
    userlist = json.loads(url.text)
    mycoll.insert_one(userlist)
    
    return userlist


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp




if __name__ == '__main__':
    app.run(debug=True)