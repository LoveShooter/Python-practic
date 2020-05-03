import pymongo
import requests
import json, bson
import random
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from flask_cors import CORS


app = Flask(__name__)
CORS(app)   # This will enable CORS for all routes


app.config['MONGO_DBNAME'] = 'userslist' # Name of database on mongo
app.config["MONGO_URI"] = "mongodb+srv://sysadm:Ff121314@cluster0-gpxwq.mongodb.net/userslist" #URI to Atlas cluster  + Auth Credentials

mongo = PyMongo(app)


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


@app.route('/deldata/<int:user_id>', methods=['GET'])
def del_one_data(user_id):
    usercoll = mongo.db.users
    usercoll.delete_one({'id': user_id}) # Delete data by user ID

    return jsonify('Task deleted successfully!')


if __name__ == '__main__':
    app.run(debug=True)