from pymongo import MongoClient
client = MongoClient('mongodb+srv://USER:PASSWORD@cluster0.irsirur.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

#주의 문자열 '0'으로 변경할 것!
db.movies.update_one({'title':'가버나움'},{'$set':{'star':'0'}})

print(db.movies.find_one({'title':'가버나움'}))
