import pymongo

client = pymongo.MongoClient("mongodb+srv://sudeepsn:Sudeep123@sudeep27.sokunim.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
d1 = {"name" : "sushanshu" , "email": "sudeep@gmail.com"}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d1)


