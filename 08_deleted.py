import pymongo
if __name__=="__main__":
    print('pyMongo')
    client=pymongo.MongoClient('mongodb://localhost:27017')
    print(client)
    db=client['Bank']
    collection=db['Details']
    
    rec1={'_id':500}    
    del1=collection.delete_one(rec1)
    # print(f'Count of Delete One: {del1.deleted_count}')

    rec2={'Name':'Mousumi Mishra'}
    del2=collection.delete_many(rec2)
    print(f'Count of Delete : {del2.deleted_count}')
    