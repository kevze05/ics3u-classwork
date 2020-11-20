#Question 1
#----------------------------------
colour = input("Hello, what is your favorite colour? ")
print(f"Hey, {colour} is my favorite colour too!")

#Question 2
#-----------------------------------
cans = int(input("How many cans are in each package? "))
packages = int(input("How many packages are there in total? "))

total = cans*packages
print(f"There are {total} cans in total.")

#Question 3
#----------------------------------
le = int(input("What is the length? "))
wi = int(input("What is the width? "))
hi = int(input("What is the height? "))

volume = le*wi*hi
print(f"The volume is of the prism is {volume}")

#Question 4
#---------------------------------
inp = input("Did you join the Google Meet and mute the teacher? (yes/no) ")

while (True):
    if (inp == "yes"):
        print("That's probably not a good idea")
        break
    elif (inp == "no"):
        print("Ok. Good.")
        break
    else:
        inp = input("Invalid input, please try again. (yes/no)")
