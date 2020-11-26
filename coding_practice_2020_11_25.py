#codingbat 
#---------------

#Question: Hello Name

def hello_name(name):
    return "Hello " + name + '!'

#Question: make_out_word

def make_out_word(out, word):
    return out[0:2] + word + out[2:5]

#Question: first_half

def first_half(str):
    return str[0:len(str)/2]

#Question: without_end

def without_end(str):
    return str[1:len(str)-1]

#Question: combo_string

def combo_string(a, b):
    if (len(a) > len(b)):
        return b + a + b
    else:
        return a+b+a
    
#Question: non_start

def non_start(a, b):
    return a[1:len(a)]+b[1:len(b)]

#Question: left2

def left2(str):
    return str[2:len(str)]+str[0:2]

#Question: make_abba

def make_abba(a, b):
    return a+b+b+a

#Question: make_tags

def make_tags(tag, word):
    return '<' + tag + '>' + word + '<' + '/' + tag + '>' 

#Question: extra_end

def extra_end(str):
    temp = str[len(str)-2:len(str)]
    return temp+temp+temp

#Question: first_two

def first_two(str):
    return str[0:2]

#Python Workbook if_else
#------------------------

#Exercise 34: Even or Odd?

integer = int(input("Enter an integer: "))
if (integer % 2 == 0):
    print(f"{integer} is even")
else:
    print(f"{integer} is odd")

#Exercise 35: Dog Years

years = int(input("How old is your dog in human years? "))

if (years < 0):
    print("Error, negative age.")
elif (years <= 2):
    print(f"Your dog is {years*10.5} dog years old.")
else:
    print(f"Your dog is {21+(years-2)*4} dog years old.")

#Exercise 36: Vowel or Consonant

letter = input("Enter a character: ")

vowels = ['a','e','i','o','u']
if ((letter not in vowels) == False):
    print(f"{letter} is a vowel.")
elif (letter == 'y'):
    print(f"Sometimes {letter} is a vowel and sometimes {letter} is a consonant.")
else:
    print(f"{letter} is a consonant.")

#Exercise 37: Name that Shape

sides = int(input("How many sides does your shape have? (3-10) "))

vowels = ["Triangle", "Square", "Penta", "Hexa", "Hepta", "Octa", "Nona", "Deca"]

if (sides < 3 or sides > 10):
    print("Invalid input.")
elif (sides < 5):
    print(f"Your shape is a {vowels[sides-3]}.")
else:
    print(f"Your shape is a {vowels[sides-3]}gon.")

#Exercise 38: Month Name to Number of Days

month = input("What month is it? ")

big = ["January", "March", "May", "July", "August", "October", "December"]

if (month == "February"):
    print(f"{month} has 28 or 29 days.")
elif (month not in big):
    print(f"{month} has 30 days.")
else:
    print(f"{month} has 31 days.")
    
#Exercise 39: Sound levels

sound = int(input("How many decibels is the sound level? "))

lb = -1
ub = -1

bench = ["Nothing", "Quiet room", "Alarm clock", "Gas lawnmower", "Jackhammer", "Way too loud"]

tf = False

if (sound < 0):
    print("The sound level is Nothing.")
    tf = True
elif (sound <= 40):
    lb = 0
    ub = 1
elif (sound <= 70):
    lb = 1
    ub = 2
elif (sound <= 106):
    lb = 2
    ub = 3
elif (sound <= 130):
    lb = 3
    ub = 4
else:
    print("The sound level is Way too loud.")    
    tf = True

if (tf == False):
    print(f"The sound level is between {bench[lb]} and {bench[ub]}.")

#Exercise 40: Name that Triangle

side1 = int(input("What is the length of the first side? "))
side2 = int(input("What is the length of the second side? "))
side3 = int(input("What is the length of the third side? "))

if (side1 == side2 and side2 == side3):
    print("The triangle is equilateral.")
elif  (side1 == side2 or side2 == side3 or side3 == side1):
    print("The triangle is isoceles.")
else:
    print("The triangle is scalene.")
    
#Exercise 44: Date to Holiday Name

month = input("What is the month? ")
day = int(input("What is the day? " ))

if (month == "January" and day == 1):
    print("It is New Year's day! ")
elif (month == "July" and day == 1):
    print("It is Canada day! ")
elif (month == "December" and day == 25):
    print("It is Christmas day! ")
else:
    print("It is not a holiday :( ")

#Exercise 45: What Colour is that Square?

pos = input("What is the position? ")

white_even = ['a','c','e','g']
white_odd = ['b','d','f','h']

letter = pos[0]
num = int(pos[1])
colour = ""

if (letter in white_even):
    if (num % 2 == 0):
        colour = "white"
    else:
        colour = "black"
else:
    if (num % 2 == 0):
        colour = "black"
    else:
        colour = "white"

print(f"{pos} is a {colour} square.")

#Exercise 57: Is it a Leap Year

year = int(input("Enter the year: "))

tf = False
if (year % 400 == 0):
    tf = True
elif (year % 100 == 0):
    tf = False
elif (year % 4 == 0):
    tf = True

if (tf == True):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
