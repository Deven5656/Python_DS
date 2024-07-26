"""
    @Author: Deven Gupta
    @Date: 26-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 26-07-2024
    @Title : Python program to create list and tuple of user input

"""

def create_list_tuple(user_input):
    """
        Description :
            This function is used to create list and tuple of user input
        Parameters :
            user_input :sequence of comma-separated numbers 
        return :
            tuple: which contain list and tuple of user input
            
    """
    num_list = user_input.split(',')

    num_tuple = tuple(num_list)

    return num_list,num_tuple


def main():
    user_input = input("Enter a sequence of comma-separated numbers: ")

    number_list,number_tuple=create_list_tuple(user_input)
    print("List :", number_list)
    print("Tuple :", number_tuple)

if __name__ == "__main__":
    main()