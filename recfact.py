


def fact(num):
    if num==0:
        return 1
    r=num*fact(num-1)
    return r


res = fact(5)
print(res)