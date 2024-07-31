""" 
    @Author: Deven Gupta
    @Date: 29-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 29-07-2024
    @Title : Python program to create the clone of a tuple.

"""
def clone_tuple(tup):
    """
        Description :
            This function is used to create the clone of a tuple
        Parameters :
            tup : input tuple
        return :
            tuple : clone of input tuple
     """
    # clone_tuple=tuple(tup)
    clone_tuple=tup[:]

    return clone_tuple
    

def main():
     input_tuple=(1,2,3,4,5,6)
     print(clone_tuple(input_tuple))
if __name__ == "__main__":
    main()
