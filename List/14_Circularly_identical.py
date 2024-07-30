""" 
    @Author: Deven Gupta
    @Date: 29-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 29-07-2024
    @Title: Python program to check whether two lists are circularly identical

"""
def circularly_identical(lst1,lst2):
    """
    Description :
        This function is used to check whether two lists are circularly identical
    Parameters :
        lst1 : first input List
        lst2 : second input list 
    return :
        boolean : True if Identical else False
    """

    lst1 = lst1 + lst1

    for index in range(len(lst1)):
        if lst2 == lst1[index : index + len(lst2)]:
            return True
    return False

                

def main():
    input_list1=[1,2,3,4,5]
    input_list2=[3,4,5,1,2]
    if circularly_identical(input_list1,input_list2) :
        print("List are circularly Identical")
    else:
        print("List are not circularly Identical")

if __name__ == "__main__":
    main()