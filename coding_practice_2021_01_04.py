#TPW 81

import math

def hypot (x, y):
    return math.sqrt(x**2+y**2)


def main():
    x = int(input("What is the length of the first leg? "))
    y = int(input("What is the length of the second leg? "))
    print(f"The length of the hypotenuse is {hypot(x,y)}.")

if __name__ == "__main__":
    main()
    
    
#TPW 82

def calc_fare (dist):
    dist = dist*1000
    return round((dist/140)*0.25,2)

def main():
    dist = int(input("What is the distance travelled in kilometers? "))
    print(f"Your fare is ${4.0+calc_fare(dist)}.")


if __name__ == "__main__":
    main()

#TPW 83

def calc_cost (items):
    return 10.95+(items-1)*2.95

def main():
    items = int(input("How many items do you need shipped? "))
    print(f"Your cost is ${calc_cost(items)}.")


if __name__ == "__main__":
    main()

#TPW 84

def find_median (a, b, c):
    li = [a,b,c];
    li.remove(max(a,b,c))
    li.remove(min(a,b,c))
    return li[0]

def main():
    a = int(input("What is the first number? "))
    b = int(input("What is the first number? "))
    c = int(input("What is the first number? "))
    print(f"The median of {a}, {b}, and {c} is {find_median(a,b,c)}.")


if __name__ == "__main__":
    main()

#TPW 85

def ordinal_num (num):
    li = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]
    if num >= 1 and num <= 12:
        return li[num-1]
    else:
        return ""
def main():
    print("The first twelve ordinal numbers are: \n")
    for i in range(1,13):
        print(ordinal_num(i))


if __name__ == "__main__":
    main()
