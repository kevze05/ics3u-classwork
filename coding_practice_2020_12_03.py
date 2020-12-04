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


num1 = 4
num2 = 5
num3 = 6
total = add3(num1, num2, num3)
print(f"The sum {num1}, {num2}, and {num3} is {total}.")

message = print_message("Bob", 15)
print(message)

num1 = 10
num2 = 20
avg = average(num1, num2)
print(f"The average of {num1} and {num2} is {avg}")

num1 = 7
num2 = 10
num3 = 15
big = largest3(num1, num2, num3)
print(f"The largest out of {num1}, {num2}, and {num3} is {big}.")

str = "Hello World"
f2 = first2(str)
print(f"The first two characters in {str} is {f2}.")

