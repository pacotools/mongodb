import pymongo
import os
import env

#from os import path
#if path.exists("env.py"):
#    import env

MONGODB_URI = os.getenv("MONGODB_URI")
#MONGODB_URI = os.environ.get("MONGODB_URI")

DBS_NAME = "myTestDB"
COLLECTION_NAME = "myFirstMDB"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e
        
conn = mongo_connect(MONGODB_URI)

coll = conn [DBS_NAME] [COLLECTION_NAME]

# (B) - Insert one document o record:
#new_doc = {'first': 'douglas', 'last': 'adams', 'dob': '11/03/1952', 'hair_colour': 'grey', 'occupation': 'writer', 'nationality': 'english'}
#coll.insert_one(new_doc)

# (C) - Insert many documents:
#new_docs = [{'first': 'terry', 'last': 'pratchett', 'dob': '28/04/1948', 'gender': 'm', 'hair_colour': 'not much', 'occupation': 'writer', 'nationality': 'english'},
#            {'first': 'george', 'last': 'rr martin', 'dob': '20/09/1948', 'gender': 'm', 'hair_colour': 'white', 'occupation': 'writer', 'nationality': 'american'}]
#coll.insert_many(new_docs)

# (D) - Find a specific record:
#documents = coll.find({'first': 'douglas'})

# (E) - Delete a specific record:
#coll.delete_one({'first': 'douglas'})

# (F) - Update ONE document with some criteria and check(find) documents with this criteria:
#coll.update_one({'nationality': 'american'}, {'$set': {'hair_colour': 'maroon'}})
#documents = coll.find({'nationality': 'american'})

# (G) - Update ALL documents #with some criteria and check(find) documents with this criteria:
#coll.update_many({'nationality': 'american'}, {'$set': {'hair_colour': 'maroon'}})
#documents = coll.find({'nationality': 'american'})

# (A) - Find all documents o records:
documents = coll.find()

for doc in documents:
    print(doc)