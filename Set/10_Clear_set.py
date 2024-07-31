""" 
    @Author: Deven Gupta
    @Date: 30-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 30-07-2024
    @Title : Python program to clear a set.

"""
def clear_set(input_set):
    """
        Description :
            This function is used to clear a set.
        Parameters :
            input_set : set with items
        return :
            set : empty set

    """
    empty_set=set()   # clear() method
    input_set=empty_set
   
    return input_set
    
def main():
    input_set ={1,2,3,4,55}
    print(clear_set(input_set))

if __name__ == "__main__":
    main()
