""" 
    @Author: Deven Gupta
    @Date: 30-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 30-07-2024
    @Title : Python program to add a key to a dictionary

"""

def add_key(input_dict):
    """
        Description :
            This function is used to add key-value to dictionary
        Parameters :
            input_dict: input dictionary
        return :
            dict
     """
    # input_dict.update({7:77})
    input_dict[7]=77
    return input_dict


def main():

    input_dict = {1: 50, 2: 20, 3: 60, 4: 40, 5: 10, 6: 30}
    print(add_key(input_dict))


if __name__ == "__main__":
    main()
