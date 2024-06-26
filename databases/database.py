from pymongo import MongoClient
import numpy as np
import os
from dotenv import load_dotenv 


def get_client():
    load_dotenv()
    url = os.getenv('local_host')
    return url

def checking_cred(name,passw):
    url=get_client()
    client = MongoClient(url) 
    db = client['DhanushWebsite']  
    collection = db['Users'] 
    users = collection.find()
    x=False
    for user in users:
        # print(user)
        if user['username']==name and user['password']==passw :
                x=True
    return x
    
def adding_new(new_user):
    url=get_client()
    client = MongoClient(url) # Update this with your MongoDB URI
    db = client['DhanushWebsite']  # Replace 'your_database_name' with your database name
    collection = db['Users']
    collection.insert_one(new_user)
    return True

def add_test_data(name,data,subject):
    url=get_client()
    client = MongoClient(url) 
    db = client['DhanushWebsite']
    collection = db['Users']
    document = collection.find_one({"username": name})
    new_data = {"data":[data[0],data[1],data[2],data[3]],"subject":f"{subject}"}
    collection.update_one({"_id": document["_id"]}, {"$push": {"test": new_data}})
    print('New test data has been added')
    return True

def retrieve_test_data(name):
    url=get_client()
    client = MongoClient(url) 
    db = client['DhanushWebsite']
    collection = db['Users']
    document = collection.find_one({"username": name})
    json_data = []
    if document is not None and "test" in document:
        test_data = document["test"]
        for item in test_data:
            subject = item["subject"]
            data = item["data"]
            json_data.append({"Subject": subject,"Score": data[0], "Wrong":data[1],"Attempted":data[2],"Unattempted":data[3]})
        return json_data

    else:
        print("No 'test' field found in the document.")
        return json_data
    
def retrieve_avg_data(name):
    url=get_client()
    client = MongoClient(url) 
    db = client['DhanushWebsite']
    collection = db['Users']
    document = collection.find_one({"username": name})
    all_data=[]
    number=0
    conv_avg_data=0
    if document is not None and "test" in document:
        test_data = document["test"]
        for item in test_data:
            subject = item["subject"]
            data = item["data"]
            all_data.append(data)
            number+=1
            # print(subject,data)
        all_data=np.array(all_data) 
        avg_data=np.average(all_data,axis=0)
        conv_avg_data=convert_to_one_decimal(avg_data)
        
    else:
        conv_avg_data=[0,0,0,0]
    
    return conv_avg_data,number
    

def convert_to_one_decimal(arr):
    return [round(num, 1) for num in arr.tolist()] 

def retrieve_plot_data(name):
    url=get_client()
    client = MongoClient(url) 
    db = client['DhanushWebsite']
    collection = db['Users']
    document = collection.find_one({"username": name})
    correct=[]
    subjects=[]
    if document is not None and "test" in document:
        test_data = document["test"]
        for item in test_data:
            subject = item["subject"]
            data = item["data"]
            correct.append(data[0])
            subjects.append(subject)
    else:
        correct=[0]
        subject=['']
    data={'labels':subjects,'values':correct}
    return data
    

        

# if __name__=="__main__":
#     print(retrieve_avg_data('bunty'))