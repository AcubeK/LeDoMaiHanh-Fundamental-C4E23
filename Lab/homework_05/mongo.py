#mongodb://admin:admin@ds021182.mlab.com:21182/c4e

# host = "ds021182.mlab.com"
# port = 21182
# db_name = "c4e"
# username = "admin"
# password = "admin"

from pymongo import MongoClient 

uri ="mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)
db = client.get_database()
posts = db["posts"]

new = {
    "title": "Review",
    "author": "Anon",
    "content": "Thực sự thấy vui vẻ khi học và theo đuổi :)"
}

posts.insert_one(new)
client.close()
