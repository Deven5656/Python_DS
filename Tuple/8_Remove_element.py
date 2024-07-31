""" 
    @Author: Deven Gupta
    @Date: 29-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 29-07-2024
    @Title : Python program to remove an item from a tuple.

"""
def remove_element(tup,value):
    """
        Description :
            This function is used to remove an item from a tuple
        Parameters :
            tup : input tuple
        return :
            tuple : tuple after removing element
    """


    while value in tup:
        index=tup.index(value)
        tup=tup[:index]+tup[index+1:]

    return tup


def main():
     input_tuple=(1,2,3,4,5,6,5,7)
     value=5
     print(remove_element(input_tuple,value))

if __name__ == "__main__":
    main()
