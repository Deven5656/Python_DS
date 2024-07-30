""" 
    @Author: Deven Gupta
    @Date: 29-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 29-07-2024
    @Title : Python program to sum all the items in a list

"""
def list_sum(lst):
    """
    Description :
        This function is used to add all element in list
    Parameters :
        lst : input List of number
    return :
        int : sum of list by adding element of list
    """
    sum = 0
    for element in lst:
        sum = sum + element
    return sum

def main():
    number_list=[1,2,3,4,5]
    print(list_sum(number_list)) 

if __name__ == "__main__":
    main()