# write a program that asks users to enter a number and then calculates factorial of n: (1 * 2 * 3 *... *n)

print("Factorial calculator.")
n = int(input("Please enter: n = "))
x = 1

if n<0:
    print("Negative numbers are not valid to calculate factorial.")
elif n==0:
    print("The factorial of 0 equals 1.")
else:
    for i in range(1, n+1):
        x = x*i
    
    print("The factorial of", n, "equals", x)
