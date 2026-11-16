# a=3
# b=4
# print(a/0)

try:                     # part that contains the program
    a = 10  
    b = int(input("enter a value"))
    print(a/b)
except ZeroDivisionError:     # this block will excecute hen an error occurs in the code written in the try block
    print("ZeroDivisionError")
except ValueError:     
    print("Enter a valid value")
else:                          #  this will execute when try block runs without an error 
    print("division is Succesfully Completed")
finally:                       # it will be executed wether an error occurs or not
    print("your task is completed")    # it can be usd to secure file operation, cleanup operation and propper resourse management

# a=int(input("enter your age:"))
# print(a)