# https://www.codewithharry.com/blogpost/mongodb-cheatsheet/   
# Follow this one

import pymongo
if __name__=="__main__":
    print('pyMongo')
    client=pymongo.MongoClient('mongodb://localhost:27017')
    print(client)
    db=client['Rahul']
    collection=db['sampleCollection']
    data=[]
    collection.insert_one(
        {
            '__id':20023,
            'Name':'Anirban Mishra',
            'Dept.':'CSE'
        }
    )
    collection.insert_many(
        {
            'Name':'abc',
            'Roll':'100'
        },
        {
            'Name':'def',
            'Roll':'200'
        }
    )