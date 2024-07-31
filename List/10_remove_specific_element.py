""" 
    @Author: Deven Gupta
    @Date: 29-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 29-07-2024
    @Title: Python program to print a specified list after removing the 0th, 4th and 5th elements.

"""
def remove_specific_element(lst):
    """
    Description :
        This function is used to get specified list after removing the 0th, 4th and 5th elements
    Parameters :
        lst : input List
    return :
        list : after removing specific element
    """

    # new_list=[ele for ele in lst if ele!=lst[0] and ele!=lst[4] and ele!=lst[5] ]    #List comprehension

    new_list=[]
    for element in lst:
        if  element!=lst[0] and element!=lst[4] and element!=lst[5] :
            new_list.append(element)

    return new_list
  

def main():
    input_list=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    print(remove_specific_element(input_list)) 

if __name__ == "__main__":
    main()