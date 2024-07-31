""" 
    @Author: Deven Gupta
    @Date: 29-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 29-07-2024
    @Title: Python program to find common items from two lists.


"""
def common_item(lst1,lst2):
    """
    Description :
        This function is used to find common items from two lists.
    Parameters :
        lst1 : first input List
        lst2 : second input list 
    return :
        list : list with common element
    """
    common_item_list=[]

    for element in lst1:
        if element in lst2:
            common_item_list.append(element)

    return common_item_list
                

def main():
    input_list1=['Red', 'Green', 'White', 'Black', 'Yellow',2]
    input_list2=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow',1,2]
    print(common_item(input_list1,input_list2)) 

if __name__ == "__main__":
    main()