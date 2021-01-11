#Name: Kevin
#Date: December 10 2020
#Code:


#MAIN.PY


from typing import List


def get_name() -> str:
    error = ""
    while True:
        name = input("Enter a name here: ")
        if len(name) < 2:
            error = "short"
        elif len(name) > 15:
            error = "long"
        else:
            break
        print(f"Entered name is too {error}. Please try again.")
    return name


def print_welcome_message(teacher_name: str) -> str:
    return f"Hello, {teacher_name}. Welcome to the Markbook Program."


def get_num() -> int:
    while True:
        try:
            num = int(input("Enter a positive integer: "))
            if (num < 0):
                print("Input integer cannot be negative, please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please try again.")
        
    return num


def print_students(student_names: List[str], student_marks: List[int]) -> None:
    for i in range(len(student_names)):
        print(student_names[i], student_marks[i])


def fail_num(student_marks: List[int]) -> int:
    fails = 0
    for i in student_marks:
        if i < 50:
            fails += 1
    return fails


def average_mark(student_marks: List[int]) -> float:
    total = 0
    for i in student_marks:
        total += i
    return total/len(student_marks)


def main():
    student_names = []
    student_marks = []
    teacher_name = get_name()
    print(print_welcome_message(teacher_name), "\n")
    print("How many students would you like to enter? ")
    num_students = get_num()
    for i in range(num_students):
        student_names.append(get_name())
        student_marks.append(get_num())
        print()
    print_students(student_names, student_marks)
    fails = fail_num(student_marks)
    if fails == 1:
        print(f"1 student is failing the class.")
    else:
        print(f"{fail_num(student_marks)} students are failing the class.")
    
    print()
    print(f"The class average is {average_mark(student_marks)}.")


if __name__ == "__main__":
    main()


#TEST_MAIN.PY


from main import print_welcome_message, fail_num, average_mark

def test_print_welcome_message():
    assert print_welcome_message("bob") == "Hello, bob. Welcome to the Markbook Program."
    assert print_welcome_message("jack") == "Hello, jack. Welcome to the Markbook Program."
    assert print_welcome_message("abcdef") == "Hello, abcdef. Welcome to the Markbook Program."
    assert print_welcome_message("gg") == "Hello, gg. Welcome to the Markbook Program."
    assert print_welcome_message("cam") == "Hello, cam. Welcome to the Markbook Program."

def test_fail_num():
    assert fail_num([100, 100, 100, 100]) == 0
    assert fail_num([0, 0, 0, 0]) == 4
    assert fail_num([17, 45, 68, 92]) == 2
    assert fail_num([50]) == 0
    assert fail_num([49]) == 1


def test_average_mark():
    assert average_mark([100, 100, 100, 100]) == 100
    assert average_mark([0, 0, 0, 0]) == 0
    assert average_mark([17, 45, 68, 92]) == 55.5
    assert average_mark([50]) == 50
    assert average_mark([49, 50, 25, 97]) == 55.25

