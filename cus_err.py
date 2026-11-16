class MyError(Exception):
    # print("error")
    pass

# age=int(input("enter your age"))

try:
    age=int(input("enter your age"))
    if age>18:
        print("you are eligble")
        raise MyError("error")
    else:
        print("not eligible")
    # raise MyError()
except ValueError :
    print("error")
