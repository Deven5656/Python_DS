""" 
    @Author: Deven Gupta
    @Date: 29-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 29-07-2024
    @Title : Python function that takes two lists and returns True if they have at least one common member.

"""
def common_ele_list(lst1,lst2):
    """
    Description :
        This function is used to returns True if they have at least one common member.
    Parameters :
        lst1 : first input List
        lst2 : second input list 
    return :
        boolean : True or False
    """
    for element in lst1 :
        if element in lst2:
            return True
    return False


def main():
    input_list1=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    input_list2=['Deven', 'Prayag', 'Ayush', 'Shivraj', 'Pink']
    print(common_ele_list(input_list1,input_list2)) 

if __name__ == "__main__":
    main()