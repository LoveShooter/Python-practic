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
        output.append({'userId': q['userId'], 'id': q['id'], 'title': q['title'], 'completed': q['completed']})

    return jsonify({'result': output})