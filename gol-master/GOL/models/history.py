from mongoengine import*

class History(Document):
    username = StringField()
    history = ListField(StringField())