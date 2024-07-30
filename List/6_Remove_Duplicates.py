""" 
    @Author: Deven Gupta
    @Date: 29-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 29-07-2024
    @Title : Python program to remove duplicates from a list.

"""
def remove_duplicates(lst):
    """
    Description :
        This function is used to remove duplicates from a list.
    Parameters :
        lst : input List 
    return :
        list : list conatining no duplicate elements
    """
    unique_list=[]
    for element in lst:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list


def main():
    input_list=[1,2,1,34,1,4,4,"a"]
    print(remove_duplicates(input_list)) 

if __name__ == "__main__":
    main()