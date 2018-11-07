content = "Ah. Greeting."

with open("content.txt", "r") as f:
    # f.write("C o n t e n t .")
    c=f.read()
    print(c)



# #1 open file
# f = open("content.txt", "w")

# #2 write file
# f.write("C o n t e n t .")

# #3 close file
# f.close()