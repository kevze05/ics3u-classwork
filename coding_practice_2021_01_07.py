#MAIN FUNCTIONS

import pytest 

def common_end(a: list , b: list) -> list:
    """Determines whether the two lists share a common first or last element.

    Args: 
        a: the first list.
        b: the second list.

    Returns:
        True if the lists share a common first or last element, false otherwise.
    """
    return a[0] == b[0] or a[-1] == b[-1]
    

def sum3(nums: list) -> int:
    """Determines the sum of the three elements in a list.
    
    Args: 
        nums: the list.
        
    Returns:
        The sum of the three elements in the list.
    """
    return nums[0]+nums[1]+nums[2]


def rotate_left3(nums: list) -> list:
    """Rotates the elements of a list of size 3 one to the left.
    
    Args: 
        nums: the list.
        
    Returns:
        The rotated list.
    """
    li = [nums[1], nums[2], nums[0]]
    return li


def reverse3(nums):
    """Reverses the elements of a list of size 3.
    
    Args: 
        nums: the list.
        
    Returns:
        The reversed list.
    """
    li = [nums[2], nums[1], nums[0]]
    return li


def max_end3(nums):
    """Sets all elements in a list to the maximum of the first or last term.
    
    Args: 
        nums: the list.
        
    Returns:
        The new list with all elements equal to the maximum of the first or last term.
    """
    mm = max(nums[0],nums[2])
    li = [mm, mm, mm]
    return li
    
    
#PYTEST FUNCTIONS

from main import common_end
from main import sum3
from main import rotate_left3
from main import reverse3
from main import max_end3

def test_common_end():
    assert common_end([1, 2, 3], [1, 3]) == True		
    assert common_end([1, 2, 3], [7, 3, 2]) == False	
    assert common_end([1, 2, 3], [7, 3]) == True	
    assert common_end([1, 2, 3], [1]) == True	
    assert common_end([1, 2, 3], [2]) == False


def test_sum3():
    assert sum3([1, 2, 3]) == 6	
    assert sum3([5, 11, 2]) == 18	
    assert sum3([7, 0, 0]) == 7		
    assert sum3([1, 2, 1]) == 4		
    assert sum3([1, 1, 1]) == 3		
    assert sum3([2, 7, 2]) == 11		


def test_rotate_left3():
    assert rotate_left3([1, 2, 3]) == [2, 3, 1]	
    assert rotate_left3([5, 11, 9]) == [11, 9, 5]
    assert rotate_left3([7, 0, 0]) == [0, 0, 7]		
    assert rotate_left3([1, 2, 1]) == [2, 1, 1]		
    assert rotate_left3([0, 0, 1]) == [0, 1, 0]		


def test_reverse3():
    assert reverse3([1, 2, 3]) == [3, 2, 1]		
    assert reverse3([5, 11, 9]) == [9, 11, 5]		
    assert reverse3([7, 0, 0]) == [0, 0, 7]		
    assert reverse3([2, 1, 2]) == [2, 1, 2]		
    assert reverse3([1, 2, 1]) == [1, 2, 1]		
    assert reverse3([2, 11, 3]) == [3, 11, 2]		
    assert reverse3([0, 6, 5]) == [5, 6, 0]		
    assert reverse3([7, 2, 3]) == [3, 2, 7]	


def test_max_end3():
    assert max_end3([1, 2, 3]) == [3, 3, 3]		
    assert max_end3([11, 5, 9]) == [11, 11, 11]		
    assert max_end3([2, 11, 3]) == [3, 3, 3]		
    assert max_end3([11, 3, 3]) == [11, 11, 11]		
    assert max_end3([3, 11, 11]) == [11, 11, 11]		
    assert max_end3([2, 2, 2]) == [2, 2, 2]		
    assert max_end3([2, 11, 2]) == [2, 2, 2]		
    assert max_end3([0, 0, 1]) == [1, 1, 1]		
