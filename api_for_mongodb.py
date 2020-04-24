#api for mongodb data

from flask import Flask
from flask import request
from pymongo import MongoClient
import json

client = MongoClient('mongodb+srv://sysadm:Ff121314@cluster0-gpxwq.mongodb.net/')
db = client['to-do-list']

app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to Python Flask!"

#Connection to mongodb cluster, to the db 'to-do-list'
