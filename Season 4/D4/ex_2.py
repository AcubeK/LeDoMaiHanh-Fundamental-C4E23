
p = [
    {
    "Name": "Huy",
    "Hours": 30,
    "MPH":50, 
    },
    {
    "Name": "Quan",
    "Hours":20,
    "MPH": 40,
    },
    {"Name": "Duc",
    "Hours": 15,
    "MPH": 35,
    }
]

print("Numbers of hours of each person:")
for q in p:
    print(q["Name"], q["Hours"], sep = ": ")

print()

print("Wage of each person (thousands VND):")
for q in p:
    q["MW"] = q["Hours"]*q["MPH"]
    print(q["Name"], q["MW"], sep =": ")

print()

ws = 0
print("Wage sum (thousands VND): ")
for q in p:
    ws = ws + i["MW"]
print(ws)