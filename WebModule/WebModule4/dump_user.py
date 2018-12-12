import mlab 
from models.users import User

mlab.connect()
User(username = "dumb fck", password = "juice").save()

