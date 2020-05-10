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
