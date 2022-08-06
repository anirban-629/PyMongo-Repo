import pymongo
if __name__=="__main__":
    print('pyMongo')
    client=pymongo.MongoClient('mongodb://localhost:27017')
    print(client)
    db=client['Bank']
    collection=db['Details']
     
    prevDataOne={'_id':400}
    updatedDataOne={'$set':{'Salary':'100k'}}
    
    # collection.update_one(prevDataOne,updatedDataOne)

    prevDataMany={'Name':'Anup Mishra'}
    updatedDataMany={'$set':{'Salary2':'100k'},'$set':{'Salary':'70k'}}
    updatedDataMany

    count=collection.update_many(prevDataMany,updatedDataMany)

    print(count.modified_count)