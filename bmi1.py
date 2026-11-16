weight=input("enter the Weight with quantity in KG or G:")
Height=input("enter the height with quantity in M or CM:")

if weight[-2:]=="kg":
    weight=float(weight[:-2])
    print(weight)
else:
    weight=float(weight[:-1])
    weight=weight/1000
    print(weight)
if Height[-2:]=="cm":
    Height=float(Height[:-2])
    Height=Height/100
    print(Height)
else:
    Height=float(Height[:-1])
    print(Height)

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