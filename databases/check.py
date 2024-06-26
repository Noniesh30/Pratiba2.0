import pymongo
import certifi

# Ensure your connection string is correct
connection_string = 'mongodb+srv://nonieshnptel:Rf9LS77qKD8uux3Z@cluster0.hfycuqj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'

# Create a MongoClient with the certifi CA file
client = pymongo.MongoClient(connection_string, tlsCAFile=certifi.where())

# Test the connection
try:
    client.admin.command('ping')
    print("Connected to MongoDB successfully!")
except Exception as e:
    print("Error connecting to MongoDB:", e)
