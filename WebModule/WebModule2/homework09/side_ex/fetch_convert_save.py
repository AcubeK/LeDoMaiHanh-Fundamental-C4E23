from urllib.request import urlopen
from bs4 import BeautifulSoup
from mongoengine import Document, StringField, BooleanField, ListField
import json
import mlab
import html

url = "https://opentdb.com/api.php?amount=50"
conn  = urlopen(url)
data = conn.read().decode()
dict_data = json.loads(data)

test_sheet = dict_data["results"]

mlab.connect()

for t in test_sheet:

    class Q_A_sheet(Document):
        question = StringField()
        if t["type"] == "boolean":
            correct_ans = BooleanField()
            incorrect_ans = BooleanField()
        elif t["type"] == "multiple":
            correct_ans = StringField()
            incorrect_ans = ListField()

    m = Q_A_sheet(question = t["question"], correct_ans = t["correct_answer"], incorrect_ans = t["incorrect_answers"])
#     m.save()
