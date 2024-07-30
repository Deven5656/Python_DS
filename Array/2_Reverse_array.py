"""
    @Author: Deven Gupta
    @Date: 30-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 30-07-2024
    @Title : Python program to reverse the order of items in an array using the array module.
"""

import array

def reverse_array(arr):
    """
    Description :
        This function reverses the order of the items in the given array.
    Parameters :
        arr : An array of integers
    return :
        array : in reverse order
    """
    reverse_array=arr[::-1]
    return reverse_array

def main():

    integer_array = array.array('i', [10, 20, 30, 40, 50])
  
    print("Original Array",integer_array)
    
    print("Reversed Array",reverse_array(integer_array))


if __name__ == "__main__":
    main()
