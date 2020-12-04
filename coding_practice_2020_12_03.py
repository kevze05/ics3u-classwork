def add3 (a,b,c):
    return a+b+c


def print_message(name,age):
    return f"{name} is {age} years old."


def average(a,b):
    return (a+b)/2


def largest2(a,b):
    if (a > b):
        return a
    else:
        return b


def largest3(a,b,c):
    if (a > b):
        return largest2(a,c)
    elif (b > c):
        return largest2(a,b)
    elif (c > a):
        return largest2(b,c)
    else:
        return a


def first2(str):
    return str[0:2]

