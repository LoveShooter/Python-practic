@app.route('/del_data/<id>', methods=['GET'])  # Delete data by user ID
def del_one_data(id):
    db_response = mongo.db.users.delete_one({'_id': ObjectId(id)})
    if db_response.deleted_count == 1:
        response = {'message': 'Record deleted'}
    else:
        response = {'message': 'No record found!'}
    return jsonify(response), 200
