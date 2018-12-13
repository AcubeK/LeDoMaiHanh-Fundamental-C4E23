import mlab
from models.information import Information
from models.activities import Activities
from models.habit import Habit
from models.attribute import Attribute

mlab.connect()

# activity = Activities(tit = "Sleepless night", st = -2, knl = 1, cre = 0, per = 1, soc = 0)
# activity.save()

# habit = Habit(tit = "Gaming", st = 0, knl = 1, cre = 1, per = 1, soc = 0)
# habit.save()

user_list = Information.objects()
for u in user_list:
    username = u["username"]
    att = Attribute(username = username)
    att.save()