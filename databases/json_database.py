import numpy as np
import json
import os 

def load_json(file_path):
    """Load data from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_json(file_path, data):
    """Save data to a JSON file."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def add_data(file_path, new_data):
    """Add new data to the JSON file."""
    data = load_json(file_path)
    data.append(new_data)
    save_json(file_path, data)

def check_directory_exists(directory_path):
    return os.path.exists(directory_path)

def checking_cred(name,password):
    x=False
    file_path = f'json_data\{name}.json'
    if check_directory_exists(file_path):
        data = load_json(file_path)
        for entry in data:
            if entry.get("username") == name and entry.get("password") == password:
                x=True
    return x
    
def adding_new(new_user,username):
    file_path = f'json_data\{username}.json'
    add_data(file_path, new_user)
    print(f"Data added to {file_path}")
    return True

def add_test_data(name,data,subject):
    file_path = f'json_data\{name}.json'
    new_data = {"data":[data[0],data[1],data[2],data[3]],"subject":f"{subject}"}
    if check_directory_exists(file_path):
        data = load_json(file_path)
        user=data[0]
        if "test" in user:
            user["test"].append(new_data)
        else:
            user["test"] = [new_data]
    save_json(file_path,data)
    print('New test data has been added')
    return True


def retrieve_test_data(name):
    file_path = f'json_data\{name}.json'
    json_data = []
    if check_directory_exists(file_path):
        data = load_json(file_path)
        user=data[0]
        test_data = user["test"]
        for item in test_data:
            subject = item["subject"]
            data = item["data"]
            json_data.append({"Subject": subject,"Score": data[0], "Wrong":data[1],"Attempted":data[2],"Unattempted":data[3]})
        return json_data
    else:
        print("No 'test' field found in the document.")
        return json_data
    
    
def retrieve_avg_data(name):
    file_path = f'json_data\{name}.json'
    all_data=[]
    number=0
    conv_avg_data=0
    if check_directory_exists(file_path):
        data = load_json(file_path)
        user=data[0]
        test_data = user["test"]
        if len(test_data)!=0:
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
    file_path = f'json_data\{name}.json'
    correct=[]
    subjects=[]
    if check_directory_exists(file_path):
        user_data = load_json(file_path)
        user=user_data[0]
        test_data = user["test"]
        if len(test_data)!=0:
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
    





