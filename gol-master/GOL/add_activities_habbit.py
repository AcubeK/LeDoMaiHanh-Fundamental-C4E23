import mlab
from models.activities import Activities
from models.habit import Habit
mlab.connect()

activity = Activities(tit = "Sleepless night", st = -2, knl = 1, cre = 0, per = 1, soc = 0)
activity.save()

# habit = Habit(tit = "Gaming", st = 0, knl = 1, cre = 1, per = 1, soc = 0)
# habit.save()
