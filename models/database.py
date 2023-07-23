from pymongo import MongoClient
client = MongoClient("mongodb+srv://rounakdhatterwal43215:Rounak@1212@cluster0.ldgvzrm.mongodb.net/?retryWrites=true&w=majority")
db = client['PROJECTPORTFOLIO']
user = db['users']
projects=db['projects']
tasks=db['tasks']
resource=db['resources']
activeUser=db['activeUser']
count=db['counter']