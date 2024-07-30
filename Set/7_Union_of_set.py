""" 
    @Author: Deven Gupta
    @Date: 30-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 30-07-2024
    @Title : Python program to create a union of sets
    
"""
def union_set(set1,set2):
    """
        Description :
            This function is used to create a union of sets
        Parameters :
            set1 : set with items
            set2 : set with item
        return :
            set : after union
    """
    # set3 = set1 | set2  # other method
    set3 = set1.union(set2)
    
    return set3
    
def main():
    input_set1 ={1,2,3,4,55}
    input_set2 ={1,2,36,4,555}
    print(union_set(input_set1,input_set2))

if __name__ == "__main__":
    main()
