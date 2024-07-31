""" 
    @Author: Deven Gupta
    @Date: 30-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 30-07-2024
    @Title : Python program to use of frozensets.
"""
def frozen_set(input_list):
    """
        Description :
            This function is used to clear a set.
        Parameters :
            input_list : list with items
        return :
            set : frozen set
    """

    set1 = frozenset(input_list)
    
    return set1
    
def main():
    input_list =[1,2,3,4,55]
    print(frozen_set(input_list))

if __name__ == "__main__":
    main()
