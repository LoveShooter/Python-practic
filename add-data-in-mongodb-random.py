import pymongo
import random

client = pymongo.MongoClient('mongodb+srv://sysadm:Ff121314@cluster0-gpxwq.mongodb.net/')  #Connect to my MongoDB cluster + auth
db = client["random-datadb"]  #Create DB


mainmenu = ['Beef', 'Potato', 'Tomato', 'Grill', 'Vegetables', 'Chicken', 'Pesto']
drinks = ['Cola', 'Water', 'Wed wine', 'Vodka', 'Whiskey', 'White wine', 'Orange juice', 'Fanta']
dessert = ['Cake', 'Cheese cake', 'Jelly', 'Chocolate pie']
names = ['Max', 'Alex', 'John', 'Alena', 'Arnold', 'Ted', 'Philip', 'Danielle', 'Zane', 'Sirena']


for x in range(1, 11):
    orders = {
        'order_number': random.randint(1, 99),
        'guest_name': random.choice(names),
        'guest_order': random.choice(mainmenu) + ' ' + random.choice(drinks) + ' ' + random.choice(dessert)

    }

    order_result=db.peopleorders.insert_one(orders)  # add result in db + add coll 'peopleorders'
    print(x, format(order_result.inserted_id))


