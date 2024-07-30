""" 
    @Author: Deven Gupta
    @Date: 29-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 29-07-2024
    @Title : Python program to clone or copy a list

"""
def remove_duplicates(lst):
    """
    Description :
        This function is used to clone or copy a list
    Parameters :
        lst : input List 
    return :
        list : clone or copy of list
    """
    # clone_list=list(lst)
    # clone_list=lst[:]
    # clone_list = [*]
    clone_list =lst.copy()

    return clone_list


def main():
    input_list=[1,2,1,34,1,4,4,"a"]
    print(remove_duplicates(input_list)) 

if __name__ == "__main__":
    main()