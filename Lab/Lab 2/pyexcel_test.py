import pyexcel
from collections import OrderedDict
#prepare data
game_lib = [
    OrderedDict({"Title": "Undertale",
    "Genre": "Psychological Horror, Comedy"
    }),
    {"Title": "Love live School Idol Festival",
    "Genre" : "Rhythm"
    }
]

pyexcel.save_as(records = game_lib, dest_file_name = "python_test.xlsx")
#save file using save_as()
# list comprehension
