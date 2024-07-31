""" 
    @Author: Deven Gupta
    @Date: 30-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 30-07-2024
    @Title : Python program to add member(s) in a set.

"""
def add_members(input_set):
    """
        Description :
            This function is used to add member in set
        Parameters :
            input_set: input set
        return :
            set : after adding items
    """
    input_set.add(6)
    
    return input_set
def main():
    input_set ={1,2,3,4,5}
    print(add_members(input_set))

if __name__ == "__main__":
    main()
