""" 
    @Author: Deven Gupta
    @Date: 26-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 26-07-2024
    @Title : Python program to check whether a specified value is contained in a group of values.
    
"""

def check_value_in(num):
    """
        Description :
            This function is used to check whether a specified value is contained in a group of values.
        Parameters :
            num: interger number
        return :
            boolean : True or False    
    """
    lst=[1, 5, 8, 3 ,6]

    if num in lst:
        return True
    else:
        return False


def main():
    value=int(input("Enter the value to be check : "))

    print(check_value_in(value))


if __name__ == "__main__":
    main()