""" 
    @Author: Deven Gupta
    @Date: 29-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 29-07-2024
    @Title : Python program to slice a tuple

"""
def slice_tuple(tup,start,end):
    """
        Description :
            This function is used to to slice a tuple
        Parameters :
            tup : input tuple
            start : starting index
            end : ending index
        return :
            tuple : tuple after slicing
    """
    
    tup=tup[start:end]

    return tup


def main():
     input_tuple=(1,2,3,4,5,6,5,7)
     start=int(input("Starting index : "))
     end=int(input("Ending index : "))
     print(slice_tuple(input_tuple,start,end))

if __name__ == "__main__":
    main()
