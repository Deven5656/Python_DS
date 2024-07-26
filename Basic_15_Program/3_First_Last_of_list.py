""" 
    @Author: Deven Gupta
    @Date: 26-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 26-07-2024
    @Title : Python program to display the first and last colors from the list
    
"""

def first_last_element(lst):
    """
        Description :
            This function is used get first and last element of list
        Parameters :
            lst :list containing colors
        return :
            tuple: which contain first and last element
            
    """ 
    first_element=lst[0]
    last_element=lst[-1]

    return first_element,last_element


def main():
    color_list = ["Red","Green","White" ,"Black"]

    first_color,last_color=first_last_element(color_list)

    print(f"\nFirst color of list is {first_color} and Last color of list is {last_color}")

if __name__ == "__main__":
    main()