import mlab
from movie import Movie
from resource import Resource
from faker import Faker

fake = Faker('en_US')

# for i in range(10):
#     print(fake.city())

mlab.connect()

# m = Movie.objects().with_id("5bf7f9aaccffd00af0fbd55c")
# print(m.title)
# m.delete()

# r = Resource.objects().first()
# r.delete()

# resource_list = Resource.objects()

# for x in resource_list:
#     print(x.name, x.yob, x.height, x.weight, sep = "    ")
# m = Movie(title = "Batman", year = 2005)
# m.save()

# a = Resource(name = "Robert", yob = 1999, height = 168, weight = 66)
# b = Resource(name = "William", yob = 1995, height = 179, weight = 69)
# c = Resource(name = "Jule", yob = 2002, height = 167, weight = 57)
# a.save()
# b.save()
# c.save()
# from random import randint

# for _ in range(100):
#     r = Resource(name = fake.name(), city = fake.state(), yob = randint(1980, 2000), height = randint(150, 200), weight = randint(40, 100))
#     r.save()

# records = Resource.objects(name = "Lori Pierce")
# print(len(records))
# for x in records:
#     print(x.city, x.yob, x. height, x.weight, sep = "   ")

# records = Resource.objects(height = 172)
# for x in records:
#     print(x.name)


# records  = Resource.objects()

# for r in records:
#     r.update(set__available = False)

r = Resource.objects().with_id("5bf80c35ccffd01720b54164")
r.update(set__available = True)