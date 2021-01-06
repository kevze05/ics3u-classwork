#TPW 87 WITH TESTS + TRY EXCEPT

def center_string (s, w):
    ret = ""
    for i in range((w-len(s))//2):
        ret += " "
    ret += s
    return ret

def tests():
    assert center_string("a", 3) == " a"
    assert center_string("aa", 4) == " aa"
    assert center_string("b", 5) == "  b"
    assert center_string("hello", 11) == "   hello"
    print("all passed!")


def main():
    s = input("Please enter your string: ")
    while (True):
        try:
            w = int(input("Please enter the width: "))
            break
        except ValueError: 
            print("Invalid input. Please enter a integer.")
    print(center_string(s, w))


if __name__ == "__main__":
    main()
    #tests()
