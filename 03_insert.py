from http import client
from multiprocessing.connection import Client
import pymongo as p
if __name__=="__main__":
    client=p.MongoClient('mongodb://localhost:27017')
    print(client)
    database=client['Bank']
    collection=database['Details']
    data=[
        # {'Name':'Anup Mishra', 'Salary':111111},
        # {'Name':'Mousumi Mishra', 'Salary':1111111},
        {'_id':400,'Name':'Anup Mishra', 'Salary':10000},
        {'_id':500,'Name':'Mousumi Mishra', 'Salary':10000}
    ]
    collection.insert_many(data)