import re
import time


def login():
        print("welcome to the page")
        


a= input("enter your phone number:")
def phone(a):
    res=re.findall(r"[6-9]{1}+[0-9]{9}",a)
    i=1
    while i:
        if res:
            print(f"you phone number {a} is valid")
            i=0
        else:
            print("phone numner is invalid")
            a= input("please re-enter your phone number:")
            res=re.findall(r"[6-9]{1}+[0-9]{9}",a)
    return 1

phone(a)
     
    

b=input("enter your email :")

def email(b):
    rs=re.fullmatch(r"[a-zA-z0-9._/+]+@[a-z]+.[a-z]{2,}",b)
    i=1
    while i:
        if rs:
            print(f"you email {b} is valid")
            i=0
        else:
            print("email is invalid")
            b=input(" please re-enter your email :")
            rs=re.fullmatch(r"[a-zA-z0-9._/+]+@[a-z]+.[a-z]{2,}",b)
    return 1
email(b)


c=input("enter the password:")
def loggin(c):
    hai=re.fullmatch(r"[a-zA-Z0-9]{6,8}",c)
    i=1
    while i:
        if hai:
            time.sleep(2)
            print("you have successfully loggedin")
            i=0
        else:
            print("invalid password")
            c=input("re-enter the password:")
            hai=re.fullmatch(r"[a-zA-Z0-9]{6,8}",c)
    return 1
loggin(c)



    


