from pymongo import Connection

conn = Connection()

db = conn['Login']

res = db.users.find({},{'_id':False})
for r in res:
    print r

def add_user(u, pw):
    db.users.insert({'user':u, 'password':pw})

add_user("hello","goodbye")
res = db.users.find({},{'_id':False})
for r in res:
    print r
