from distutils.filelist import findall
import pymongo
if __name__=="__main__":
    print('pyMongo')
    client=pymongo.MongoClient('mongodb://localhost:27017')
    print(client)
    db=client['Bank']
    collection=db['Details']

    # suppose want to hide some data then we have to use 1 or 0
    # in a database there are fields like name and pass so i want 
    # to see the name but dont want the pass so in that case we use this

    # by default id is 1 and others are 0       |---------------------------|
    data=collection.find({'Name':'Anup Mishra'},{'Name':1,'_id':0,'Salary':1})

    print(data)
    
    for ele in data:
        print(ele)

