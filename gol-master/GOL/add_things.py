import mlab
from models.information import Information
from models.activities import Activities
from models.habit import Habit
from models.attribute import Attribute
from models.quote import Quote

mlab.connect()

# activity = Activities(tit = "Sleepless night", st = -2, knl = 1, cre = 0, per = 1, soc = 0)
# activity.save()

# habit = Habit(tit = "Gaming", st = 0, knl = 1, cre = 1, per = 1, soc = 0)
# habit.save()

quote = Quote(username = "Bucko869", quote = "Mọi con đường đều dẫn tới cái chết, liệu có cậu ở bên... mọi thứ rồi sẽ nhẹ nhàng hơn?")
quote.save()