""" 
    @Author: Deven Gupta
    @Date: 29-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 29-07-2024
    @Title : Python program to get the smallest number from a list

"""
def list_minimum(lst):
    """
    Description :
        This function is used to get the smallest number from a list
    Parameters :
        lst : input List of number
    return :
        int : smallest number of list
    """
    smallest = lst[0]
    for element in lst:
        if element < smallest :
            smallest = element
    return smallest

def main():
    number_list=[10,5,6,78,6,2]
    print(list_minimum(number_list)) 

if __name__ == "__main__":
    main()