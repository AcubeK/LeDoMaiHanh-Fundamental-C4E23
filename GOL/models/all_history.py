from mongoengine import IntField,StringField,Document

class All_history(Document):
    user = StringField()
    tit = StringField()
    des = StringField()
    img = StringField()
    st = IntField(default = 0)
    knl = IntField(default = 0)
    cre = IntField(default = 0)
    per = IntField(default = 0)
    soc = IntField(default = 0)
    