from math import *

print("Xet pt bac 2: ax^2 + bx + c = 0.")
a = int(input("Nhap a = "))
b = int(input("Nhap b = "))
c = int(input("Nhap c = "))

delta = b**2 - 4*a*c

if delta<0:
    print("Phuong trinh vo nghiem.")
elif delta==0:
    print("Phuong trinh co 1 nghiem.")
    x = -b/2/a
    print("Nghiem duy nhat:", x)

   
else:
    print("Phuong trinh co 2 nghiem.")
    x1 = (b+ sqrt(delta))/2
    x2 = (b - sqrt(delta))/2
    print("Nghiem thu nhat:", x1)
    print("Nghiem thu hai:", x2)