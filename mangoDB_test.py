import pymongo

client = pymongo.MongoClient("mongodb+srv://SagarBVG:Sairam1997@cluster0.eahnvpm.mongodb.net/?retryWrites=true&w=majority")
db = client['test']

print(db)

d= {
    "name":"sagar",
    "email":"sagar@1997",
    "surname":"gundale"
}

db1= client['monggotest']
coll= db1['test']
coll.insert_one(d)