import random

names = ['Kitchen','Animal','State', 'Tastey', 'Big','City','Fish', 'Pizza','Goat', 'Salty','Sandwich','Lazy', 'Fun']
company_type = ['LLC','Inc','Company','Corporation']
company_cuisine = ['Pizza', 'Bar Food', 'Fast Food', 'Italian', 'Mexican', 'American', 'Sushi Bar', 'Vegetarian']

for x in range(1, 11):
    business = {
        'name' : names[random.randint(0, (len(names)-1))] + ' ' + names[random.randint(0, (len(names)-1))]  + ' ' + company_type[random.randint(0, (len(company_type)-1))],
        'rating' : random.randint(1, 5),
        'cuisine' : company_cuisine[random.randint(0, (len(company_cuisine)-1))] 
    }


print (business)