"""
    @Author: Deven Gupta
    @Date: 30-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 30-07-2024
    @Title : Python program to get the number of occurrences of a specified element in an array
"""

import array

def count_occurrences(arr, element):
    """
    Description :
        This function counts the number of occurrences of a specified element in the array
    Parameters :
        arr : An array of integers.
        element : The element to count in the array.
    return :
        int :The number of occurrences of the specified element.
    """
    count = 0
    for item in arr:
        if item == element:
            count += 1
    return count

def main():
    integer_array = array.array('i', [10, 20, 30, 20, 40, 20, 50])
    
    element_to_count = 20
        
    print(f"Number of occurrences is {count_occurrences(integer_array, element_to_count)}")

if __name__ == "__main__":
    main()
