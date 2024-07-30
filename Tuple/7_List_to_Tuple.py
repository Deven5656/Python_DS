""" 
    @Author: Deven Gupta
    @Date: 29-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 29-07-2024
    @Title : Python program to convert a list to a tuple.

"""
def list_to_tuple(lst):
    """
        Description :
            This function is used to convert a list to a tuple
        Parameters :
            lst : input list
        return :
            tuple : converted tuple
     """
    converted_tuple=tuple(lst)

    return converted_tuple


def main():
     input_list=[1,2,3,4,5,6,7]
     print(list_to_tuple(input_list))
if __name__ == "__main__":
    main()
