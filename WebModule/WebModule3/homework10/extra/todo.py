from mongoengine import Document, StringField, BooleanField

class ToDo(Document):
    Name = StringField()
    Description = StringField()
    Completion_status = BooleanField(default = False)