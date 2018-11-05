# write a program that asks user their height(cm) and weight(kg), and then calculate their BMI

print("BMI calculator.")

m = float(input("Please enter your weight in kg: "))
h = float(input("Please enter your height in cm: "))

h = h/100
bmi = m/h/h

if bmi<16:
    print("You're severely underweight.")
elif bmi<18.5:
    print("You're underweight.")
elif bmi<25:
    print("You're normal.")
elif bmi<30:
    print("You're overweight.")
else:
    print("You're obese.")
