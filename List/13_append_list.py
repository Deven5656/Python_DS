""" 
    @Author: Deven Gupta
    @Date: 29-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 29-07-2024
    @Title: Python program to append a list to the second list.

"""
def append_list(lst1,lst2):
    """
    Description :
        This function is used to append a list to the second list.
    Parameters :
        lst1 : first input List
        lst2 : second input list 
    return :
        list : list after appending other list
    """

    # lst1.extend(lst2)  other methods
    # lst1=lst1+lst2

    for element in lst2:
            lst1.append(element)
    return lst1
                

def main():
    input_list1=[1,2,3,4,5]
    input_list2=[6,7,8]
    print(append_list(input_list1,input_list2)) 

if __name__ == "__main__":
    main()