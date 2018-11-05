import matplotlib


from matplotlib import pyplot

# 1. Prepare data
# 2. Prepare labels
# 3. Draw pie
# 4. Show

machine_count = [18, 4, 2]
machine_name = ["PC", "MAC", "Linux"]
pyplot.pie(machine_count, labels = machine_name, autopct = "%.2f%%", shadow = True, explode = [0, 0.2, 0])
pyplot.title("PC vs MAC vs Linux Usage")
pyplot.axis("equal")
pyplot.show()