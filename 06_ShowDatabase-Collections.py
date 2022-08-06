import pymongo
if __name__=="__main__":
    print('pyMongo')
    client=pymongo.MongoClient('mongodb://localhost:27017')
    print(client)

    allDataBases=client.list_database_names()
    print(allDataBases)
    
    db1=client['Bank'].list_collection_names()
    db2=client['Rahul'].list_collection_names()
    db3=client['anirban'].list_collection_names()
    db4=client['config'].list_collection_names()
    db5=client['local'].list_collection_names()

    for ele in db1:
        print(ele)

    for ele in db2:
        print(ele)
        
    for ele in db3:
        print(ele)

    for ele in db4:
        print(ele)

    for ele in db5:
        print(ele)