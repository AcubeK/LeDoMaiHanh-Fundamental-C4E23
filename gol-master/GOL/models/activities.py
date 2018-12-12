from mongoengine import IntField,StringField,Document

class Activities(Document):
    tit = StringField()         #title
    st = IntField()             #strength
    knl = IntField()            #knowledge
    cre = IntField()            #creativity
    per = IntField()            #personality
    soc = IntField()            #social
    