import mlab
from todo import ToDo

mlab.connect()

task = ["New to-do", "View ALL to-do", "Mark a to-do COMPLETE", "Delete a to-do", "Exit"]
while True: 
   for i, v in enumerate(task):
      print(i+1, v)
   x = int(input("Enter your command (number) : ")) - 1
   t_list = ToDo.objects()

   if task[x] == task[0]:
      name = input("Name: ")
      descrp = input("Description: ")
      t = ToDo(Name = name, Description = descrp)
      t.save()

   elif task[x] == task[1]:
      for t in t_list:
         print(t.Name, sep = "\n")

   elif task[x] == task[2]:
      for i, v in enumerate(t_list):
         print(i+1, v.Name)
      k = int(input("Which task you want to mark? ")) - 1
      t_list[k].Completion_status = True

   elif task[x] == task[3]:
      for i, v in enumerate(t_list):
         print(i+1, v.Name)
      k = int(input("Which task you want to delete? ")) - 1  
      t_list[k].delete() 
   elif x == task.index("Exit"): 
      break