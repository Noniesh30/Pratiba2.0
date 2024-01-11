from pymongo import MongoClient


def checking_cred(name,passw):
    client = MongoClient('mongodb://localhost:27017/')  # Update this with your MongoDB URI
    db = client['DhanushWebsite']  # Replace 'your_database_name' with your database name
    collection = db['Users'] 
    users = collection.find()
    x=False
    for user in users:
        # print(user)
        if user['username']==name and user['password']==passw :
                x=True
    return x
    
def adding_new(new_user):
    client = MongoClient('mongodb://localhost:27017/')  # Update this with your MongoDB URI
    db = client['DhanushWebsite']  # Replace 'your_database_name' with your database name
    collection = db['Users']
    collection.insert_one(new_user)
    return True
