import pprint

import pymongo as pyM

client = pyM.MongoClient("mongodb+srv://byttencourt:f8KO9WI5kiJcfVgw@cluster0.akjoa5z.mongodb.net/?retryWrites=true&w=majority")

db = client.test
posts = db.posts


for post in posts.find():
    pprint.pprint(post)

print(f'total de posts {posts.count_documents({})}')

print(posts.count_documents({'author': 'Jose'}))
print(posts.count_documents({'tags': 'insert'}))

print('recuperando posts de maneira ordenada')
for post in posts.find({}).sort('date'):
    pprint.pprint(post)
