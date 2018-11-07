from pymongo import MongoClient 
from matplotlib import pyplot

uri ="mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)
db = client.get_database()

customers = db["customers"]
datalist = customers.find()

number_cus = 0
survey_ref = []
count = []
for n in datalist:
    number_cus += 1
    if n["ref"] not in survey_ref:
        survey_ref.append(n["ref"])
        count.append(1)
    else:
        for i in range(len(survey_ref)):
            if n["ref"] == survey_ref[i]:
                count[i] +=1

pyplot.pie(count, labels = survey_ref, autopct="%.2f%%")
pyplot.axis("equal")
pyplot.title("Customers' references: ")
pyplot.show()

