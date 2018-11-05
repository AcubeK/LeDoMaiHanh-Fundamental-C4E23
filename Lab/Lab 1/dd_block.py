
from pymongo import MongoClient 
uri ="mongodb://bucko:AK0489x6@ds249623.mlab.com:49623/a"

#collection -> document

# 1 Connect
client = MongoClient(uri)

# 2 Get Default database
db = client.get_database()

# 3 Get collection
posts = db["posts"]
movies = db["movies"]
# 4 Create database
new_post = {
"Title": "Sunny today",
"Content":"stillgore",
}
        # }
        # # 5 Insert data
        # posts.insert_one(new_post)
# new_movie = {
#     "Name": "Death of mine",
#     "Rating": "None becausue life never expect you to expect it fully."
# }

# movies.insert_one(new_movie)

# 5 Read data
post_list = posts.find()
# p = post_list[2]
for p in post_list:
    print(p["Title"])
    print(p["Content"])
    print("-------")
# 6 Close connectiom
client.close()