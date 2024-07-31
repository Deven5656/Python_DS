""" 
    @Author: Deven Gupta
    @Date: 30-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 30-07-2024
    @Title : Python program to create a symmetric difference.
    
"""
def symm_diff_set(set1,set2):
    """
        Description :
            This function is used to create a symmetric difference.
        Parameters :
            set1 : set with items
            set2 : set with item
        return :
            set : after symmetric difference.
    """
    # set3 = set1 ^ set2  # other method
    set3 = set1.symmetric_difference(set2)
    
    return set3
    
def main():
    input_set1 ={1,2,3,4,55}
    input_set2 ={1,2,36,4,555}
    print(symm_diff_set(input_set1,input_set2))

if __name__ == "__main__":
    main()
