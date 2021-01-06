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

#ASSERTION PRACTICE USING CODINGBAT TESTS

def first_last6(li):
    if li[0] == 6 or li[-1] == 6:
        return True
    else:
        return False

def same_first_last(li):
    if (len(li) == 0):
        return False
    elif li[0] == li[-1]:
        return True
    else:
        return False

def test_same_first_last():
    assert same_first_last([1, 2, 3]) == False
    assert same_first_last([1, 2, 3, 1]) == True
    assert same_first_last([1, 2, 1]) == True
    assert same_first_last([7]) == True
    assert same_first_last([]) == False
    print("All passed!")

def test_first_last6():
    assert first_last6([1, 2, 6]) == True
    assert first_last6([6, 1, 2, 3]) == True
    assert first_last6([13, 6, 1, 2, 3]) == False
    assert first_last6([13, 6, 1, 2, 6]) == True
    assert first_last6([3, 2, 1]) == False
    print("All passed!")

    
def main():
    pass

if __name__ == "__main__":
    main()
    test_first_last6()
    test_same_first_last()

