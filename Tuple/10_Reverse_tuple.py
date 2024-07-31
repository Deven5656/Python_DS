""" 
    @Author: Deven Gupta
    @Date: 29-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 29-07-2024
    @Title : Python program to reverse a tuple.

"""
def reverse_tuple(tup):
    """
        Description :
            This function is used to reverse a tuple.
        Parameters :
            tup : input tuple
        return :
            tuple : reverse tuple
    """
    
    reverse_tuple=tup[::-1]
    
    
    # reverse_tuple=[]
    # for item in tup:
    #     reverse_tuple.insert(0,item)

    return reverse_tuple
     

def main():
     input_tuple=(1,2,3,4,5,6,5,7)
     print(reverse_tuple(input_tuple))

if __name__ == "__main__":
    main()
