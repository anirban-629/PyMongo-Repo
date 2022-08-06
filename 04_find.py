from distutils.filelist import findall
import pymongo
if __name__=="__main__":
    print('pyMongo')
    client=pymongo.MongoClient('mongodb://localhost:27017')
    print(client)
    db=client['Bank']
    collection=db['Details']

    # One data fetch
    one=collection.find_one()
    print(one)
    
    # Customized Data fetch
    
    custom1=collection.find_one(
        {
            'name':'Mousumi Mishra'
        }
    )
    print(custom1) # output none as the all the things are case sensitive

    custom2=collection.find_one(
        {
            'Name':'Mousumi Mishra'
        }
    )

    print(custom2)

    # all object

    findAll=collection.find(
        {
            'Name':'Anup Mishra'
        }
    )
    print('All -> ')
    print(findAll) # It'll give objects now we to print it using iteration
    for ele in findAll:
        print(ele)

    
    