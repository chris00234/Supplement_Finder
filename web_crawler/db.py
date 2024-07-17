from pymongo.mongo_client import MongoClient
import json

#mongodb connection setup
client = MongoClient("mongodb+srv://songhn:<password>@supplementfinder.dixkhdi.mongodb.net/?retryWrites=true&w=majority&appName=SupplementFinder")
db = client['SupplementFinder']
collection=db['VitaminsMinerals']

#Load Json Data from file
with open('product.json','r') as json_file:
    data = json.load(json_file)

if isinstance(data,list):
    collection.insert_many(data)
else:
    collection.insert_one(data)

print("Data inserted sucessfully")



    