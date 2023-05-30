import pprint
from datetime import datetime

import pymongo as pyM

client = pyM.MongoClient("mongodb+srv://byttencourt:f8KO9WI5kiJcfVgw@cluster0.akjoa5z.mongodb.net/?retryWrites=true&w=majority")

#criando collection
db = client.test
collections = client.test.test_collection

print(db.test_collection_names)

# definição para compor o doc
post = {
    'author': 'NINO',
    'text': 'My first mongo db application on python',
    'tags': ['mongodb', 'python', 'pymongo'],
    'date': datetime.utcnow()
}

posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)
#print(db.list_collection_names())


#bulk inserts
new_posts = [{
    'author': 'NINO',
    'text': 'Outro post',
    'tags': ['bulk', 'insert', 'insert'],
    'date': datetime.utcnow()
    },
    {
    'author': 'NIco',
    'text': 'Post do Nicolas',
    'tittle': 'Mongo is fun',
    'date': datetime(2018, 3, 15, 19, 12)
    }
]
result = posts.insert_many(new_posts)
print(result.inserted_ids)

print('Recuperação final')
pprint.pprint(db.posts.find_one({'author': 'NIco'}))

for post in posts.find():
    pprint.pprint(post)
    print('----')
