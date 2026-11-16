weight=float(input("enter the Weight in KG:"))
Height=float(input("enter the height in meters:"))
bmi=weight/(Height**2)
print(bmi)
if bmi<18.5:
    print("you are under Weight")
elif bmi>=18.5 and bmi<=24.9:
    print("you are Under wieght")
elif bmi>=25 and bmi<=29.9:
    print("you are over weight")
else:
    print("you are obese")            