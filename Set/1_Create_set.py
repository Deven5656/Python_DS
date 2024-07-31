""" 
    @Author: Deven Gupta
    @Date: 30-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 30-07-2024
    @Title : Python program to create a set

"""
def create_set():
    """
        Description :
            This function is used to create set
        Parameters :
            none
        return :
            set : containing number
    """
    
    num_set = {1,2,3,4,5}
    print(type(num_set))
    
    return num_set
def main():
    print(create_set())

if __name__ == "__main__":
    main()
