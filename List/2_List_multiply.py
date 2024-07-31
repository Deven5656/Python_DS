""" 
    @Author: Deven Gupta
    @Date: 29-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 29-07-2024
    @Title : Python program to multiplies all the items in a list.

"""
def list_multiply(lst):
    """
    Description :
        This function is used to multiplies all element in list
    Parameters :
        lst : input List of number
    return :
        int : multiplication of elements in list
    """
    product = 1
    for element in lst:
        product = product * element
    return product

def main():
    number_list=[1,2,3,4,5]
    print(list_multiply(number_list)) 

if __name__ == "__main__":
    main()