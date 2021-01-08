import math

#TPW 81

def hypot (x: int, y: int) -> float:
    """
    Determines the hypotensue of a right-angled triangle with legs of length x and y.

    Args:
        x: length of the first leg.
        y: length of the second leg.

    Returns:
        The length of the hypotensue of a right-angled triangle with legs of length x and y.
    """

    return math.sqrt(x**2+y**2)

    
#TPW 82

def calc_fare (dist: int) -> float:
    """
    Determines the fare of a taxi trip based on the distance travelled in kilometers.

    Args:
        dist: distance travelled in kilometers.

    Returns:
        The cost of the trip in dollars. 
    """

    dist = dist*1000
    return round((dist/140)*0.25,2)


#TPW 83

def calc_cost (items: int) -> float:
    """
    Determines the cost of shipping based on the number of items you need to ship.

    Args:
        items: the number of items needed to be shipped.

    Returns:
        The total cost of shipping.
    """

    return round(10.95+(items-1)*2.95,2)


#TPW 84

def find_median (a: int, b: int, c: int) -> int:
    """
    Determines median of three numbers.

    Args:
        a: the first number.
        b: the second number.
        c: the third number.

    Returns:
        The median of the three numbers.
    """

    li = [a,b,c];
    li.remove(max(a,b,c))
    li.remove(min(a,b,c))
    return li[0]


#TPW 85

def ordinal_num (num: int) -> str:
    """
    Determines the ordinal representation of the first twelve numbers.

    Args:
        num: the number to be converted to ordinal form.

    Returns:
        The ordinal representation of the number.
    """

    li = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]
    if num >= 1 and num <= 12:
        return li[num-1]
    else:
        return ""


#TEST SUITE FOR ABOVE FUNCTIONS USING PYTEST

from main import hypot, calc_fare, calc_cost, find_median, ordinal_num

def test_hypot():
    assert hypot(3,4) == 5
    assert hypot(6,8) == 10
    assert hypot(5,12) == 13
    assert hypot(8,15) == 17
    assert hypot(7,24) == 25


def test_calc_fare():
    assert calc_fare(5) == 8.93
    assert calc_fare(15) == 26.79
    assert calc_fare(26) == 46.43
    assert calc_fare(12) == 21.43
    assert calc_fare(1) == 1.79


def test_calc_cost():
    assert calc_cost(5) == 22.75
    assert calc_cost(15) == 52.25
    assert calc_cost(26) == 84.70
    assert calc_cost(12) == 43.40
    assert calc_cost(1) == 10.95


def test_find_median():
    assert find_median(3,4,5) == 4
    assert find_median(6,8,100) == 8
    assert find_median(16,5,12) == 12
    assert find_median(8,15,1) == 8
    assert find_median(100,0,150) == 100


def test_ordinal_num():
    assert ordinal_num(1) == "first"
    assert ordinal_num(2) == "second"
    assert ordinal_num(3) == "third"
    assert ordinal_num(10) == "tenth"
    assert ordinal_num(18) == ""
