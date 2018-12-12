from mongoengine import Document,IntField,StringField

class Habit(Document):
    tit = StringField()
    bnf = StringField() #benefit
    streak = IntField()
    st = IntField()
    knl = IntField()
    cre = IntField()
    per = IntField()
    soc = IntField()    