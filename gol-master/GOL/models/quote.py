from mongoengine import *

class Quote(Document):
    username = StringField()
    quote = StringField()
    author = StringField(default = "Anonymous")