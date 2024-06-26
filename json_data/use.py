import json

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

if __name__ == "__main__":
    file_path = 'json_data\cred.json'
    
    # Example new data to add
    new_data = {
        "name": "hi Doe",
        "age": 60,
        "city": "New York"
    }
    
    add_data(file_path, new_data)
    print(f"Data added to {file_path}")
