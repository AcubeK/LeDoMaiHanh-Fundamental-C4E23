import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds027751.mlab.com:27751/gol

host = "ds027751.mlab.com"
port = 27751
db_name = "gol"
user_name = "admin"
password = "admin1"

def connect():
    mongoengine.connect(db_name, host = host, username = user_name, port = port, password = password)
    