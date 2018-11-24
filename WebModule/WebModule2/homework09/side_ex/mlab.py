import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds219051.mlab.com:19051/webmodule2

host = "ds219051.mlab.com"
port = 19051
db_name = "webmodule2"
user_name = "admin"
password = "admin1"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

