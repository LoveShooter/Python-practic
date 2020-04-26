#api for mongodb data
import pymongo
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
#from pymongo import MongoClient

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'to-do-lists' # name of database on mongo
app.config["MONGO_URI"] = "mongodb+srv://sysadm:Ff121314@cluster0-gpxwq.mongodb.net/to-do-lists"

mongo = PyMongo(app)

@app.route('/getdata', methods=['GET'])  # find all data in my collection
def get_all_data():
    todos = mongo.db.todos #connect to my collection

    output = []

    for q in todos.find():   # q - like query
        output.append({'owner_name': q['owner_name'], 'task_name': q['task_name'], 'priority': q['priority']})

    return jsonify({'result': output})



@app.route('/getdata/<name>', methods=['GET'])
def get_one_data(name):
    todos = mongo.db.todos
    q = todos.find_one({'owner_name': name}) # find data by owner name
    if q:
        output = {'owner_name': q['owner_name'], 'task_name': q['task_name'], 'priority': q['priority']}
    else:
        output = 'No results found'

    return jsonify({'result': output})



@app.route('/adddata', methods=['POST']) # add data in db. Need input JSON-like data.
def add_data():
    todos = mongo.db.todos
    
    _owner_name = request.json['owner_name']
    _task_name = request.json['task_name']
    _priority = request.json['priority']

    todos_id = todos.insert({'owner_name': _owner_name, 'task_name': _task_name, 'priority': _priority})
    new_todos = todos.find_one({'_id': todos_id})

    output = {'owner_name': new_todos['owner_name'], 'task_name': new_todos['task_name'], 'priority': new_todos['priority']}

    return jsonify({'result': output})



@app.route('/deldata/<taskname>', methods=['DELETE'])
def del_one_data(taskname):
    todos = mongo.db.todos
    todos.delete_one({'task_name': taskname}) # delete data by task name

    return jsonify('Task Delete Sucefully')





if __name__ == '__main__':
    app.run(debug=True)