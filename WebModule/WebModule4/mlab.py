
#mongodb://<dbuser>:<dbpassword>@ds063889.mlab.com:63889/webmodule4

import mongoengine


host = "ds063889.mlab.com"
port = 63889
db_name = "webmodule4"
user_name = "admin"
password = "admin1"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)