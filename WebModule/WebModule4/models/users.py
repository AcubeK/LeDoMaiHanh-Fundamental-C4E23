from mongoengine import Document, StringField

class User(Document):
    username = StringField()
    password = StringField()


#test
if  __name__ == "__main__":

    print("User----")