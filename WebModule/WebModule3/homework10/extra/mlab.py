import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds119734.mlab.com:19734/webmodule3

host = "ds119734.mlab.com"
port = 19734
db_name = "webmodule3"
user_name = "admin"
password = "admin1"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)
