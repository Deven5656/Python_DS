""" 
    @Author: Deven Gupta
    @Date: 27-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 27-07-2024
    @Title : Python program to reverse a string.

"""

def reverse_string(string):
    """
    Description :
        This function is used to reverse the string
    Parameters :
        string: The input string
    return :
        str: in reverse order
    """
    rev=""
    for char in string:
        rev= char + rev 

    return rev
        

def main():
    string = "abcdef"
    print(reverse_string(string))
  
if __name__ == "__main__":
    main()
   