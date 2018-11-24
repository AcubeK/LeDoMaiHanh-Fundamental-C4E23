import mlab
from river import River

mlab.connect()

r_ex2_list = River.objects(continent = "Africa")
print(len(r_ex2_list))
for r in r_ex2_list:
    print(r.name)

print("-----")
r_ex3_list = River.objects(continent = "S. America", length__lt = 1000)
print(len(r_ex3_list))
for r in r_ex2_list:
    print(r.name)