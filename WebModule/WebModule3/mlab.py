import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds135384.mlab.com:35384/register

host = "ds135384.mlab.com"
port = 35384
db_name = "register"
user_name = "admin"
password = "admin1"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())