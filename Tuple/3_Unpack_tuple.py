""" 
    @Author: Deven Gupta
    @Date: 29-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 29-07-2024
    @Title : Python program to unpack a tuple in several variables.
"""
def unpack_tuple():
    """
        Description :
            This function is used to unpack a tuple in several variables
        Parameters :
            none
        return :
            tuple 
     """
    num_tuple=(1,2,3)
    return num_tuple
    


def main():
     num1,num2,num3=unpack_tuple()
     print(num1,num2,num3)
if __name__ == "__main__":
    main()
