"""
    @Author: Deven Gupta
    @Date: 30-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 30-07-2024
    @Title : Python program to remove the first occurrence of a specified element from an array
"""

import array

def remove_first_occurrence(arr, element):
    """
    Description :
        This function removes the first occurrence of a specified element from the array
    Parameters :
        arr : An array of integers.
        element : The element to remove from the array.
    return :
        bool: True if the element was removed, False if the element was not found.
    """
    try:
        arr.remove(element)
        return arr
    
    except ValueError:
        return f"Element not found"

def main():
    integer_array = array.array('i', [10, 10, 20, 30, 40, 50])

    element_to_remove = 10

    print(remove_first_occurrence(integer_array, element_to_remove))
    

if __name__ == "__main__":
    main()
