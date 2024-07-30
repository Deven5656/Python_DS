""" 
    @Author: Deven Gupta
    @Date: 29-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 29-07-2024
    @Title : Python program to check whether an element exists within a tuple.

"""
def check_element(tup,ele):
    """
        Description :
            This function is used to check whether an element exists within a tuple
        Parameters :
            tup : input tuple
            ele : element to be checked
        return :
            boolean : True if present else False
     """
    
    for item in tup:
        if item == ele:
            return True
    return False


def main():
     input_tuple=(1,2,2,3,3,4,5,5,6)
     element=int(input("enter element to be checked : "))
     if check_element(input_tuple,element):
         print("Element present in tuple")
     else:
         print("Element not present in tuple")
if __name__ == "__main__":
    main()
