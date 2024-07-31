""" 
    @Author: Deven Gupta
    @Date: 26-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 26-07-2024
    @Title : Python program to concatenate all elements in a list into a string and return it

"""
def concate_list(lst):
    """
        Description :
            This function is used to concatenate all elements in a list into a string and return it
        Parameters :
            lst: list of elements
        return :
            string : after concatenating all elements
    """
    
    concatenated_string = '' 
    for element_in_list in lst:
        concatenated_string += str(element_in_list)  
    return concatenated_string

def main():

    lst = [1,2,3,"D","E","V"] 
    print("Concatenated string is", concate_list(lst))  

if __name__ == '__main__':
    main()  