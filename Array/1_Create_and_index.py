"""
    @Author: Deven Gupta
    @Date: 30-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 30-07-2024
    @Title : Python program to create and display array items using array module.
"""

import array

def main():
    """
    Description :
        This function creates an array of 5 integers and displays each item
        by accessing it through its index.
    Parameters :
        None
    return :
        None
    """
    integer_array = array.array('i', [10, 20, 30, 40, 50])
    
   
    print("Array items:")
    for index in range(len(integer_array)):
        print(integer_array[index],end=" ")

if __name__ == "__main__":
    main()
