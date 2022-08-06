import pymongo
if __name__=="__main__":
    print('pyMongo')
    client=pymongo.MongoClient('mongodb://localhost:27017')
    print(client)
    db=client['Rahul']
    collection=db['sampleCollection']
    data=[]
    n=int(input('How many Users You want to add: '))
    for i in range(n):
        flag_int=True
        print(f'Enter Data for Customer {i+1} --> ')
        fname=input('Enter First Name  : ')
        lname=input('Enter Last Name   : ')
        email=input('Enter Email Id.   : ')
        while(flag_int):
            try:
                ph=int(input('Enter Phone No.  : '))
                flag_int=False
            except:
                print('Enter Number..!')
        flag_int=True
        while(flag_int):
            try:
                age=int(input('Enter your age  : '))
                flag_int=False
            except:
                print('Enter Number..!')
        flag_int=True
        while(flag_int):
            try:
                balance=int(input('Enter Amount : '))
                flag_int=False
            except:
                print('Enter Number..!')
        list_data={
            'First Name':fname,
            'Last Name':lname,
            'Email':email,
            'Phone no.':ph,
            'Age':age,
            'Balance':balance
        }
        data.append(list_data)
    
    print(len(data))

    # collection.insert_one(dict1)
    # for ele in data:
    #     print(ele)
    #     collection.insert_one(ele)

    collection.insert_one({
        '__id':20023,
        'Name':'Anirban Mishra',
        'Dept.':'CSE'
    })