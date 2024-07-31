""" 
    @Author: Deven Gupta
    @Date: 30-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 30-07-2024
    @Title : Python program to iterate over dictionaries using for loops.

"""

def iterate_dict(dic1):
    """
        Description :
            This function is used to iterate over dictionaries using for loops.
        Parameters :
            dic1: input dictionary
        return :
            none
     """

    for key,value in dic1.items():
        print(f"The Key is {key} and The value is {value}")
  
def main():

    dic1={1:10, 2:20, 3:30, 4:40, 5:50, 6:60}

    iterate_dict(dic1)


if __name__ == "__main__":
    main()
