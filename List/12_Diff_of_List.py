""" 
    @Author: Deven Gupta
    @Date: 29-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 29-07-2024
    @Title: Python program to get the difference between the two lists.


"""
def diff_of_list(lst1,lst2):
    """
    Description :
        This function is used to get the difference between the two lists.
    Parameters :
        lst1 : first input List
        lst2 : second input list 
    return :
        list : list with different element
    """
    diff_list=[]

    for element in lst1:
        if element not in lst2:
            diff_list.append(element)

    for element in lst2:
        if element not in lst1:
            diff_list.append(element)

    return diff_list
                

def main():
    input_list1=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow',2]
    input_list2=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow',1,2]
    print(diff_of_list(input_list1,input_list2)) 

if __name__ == "__main__":
    main()