""" 
    @Author: Deven Gupta
    @Date: 27-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 27-07-2024
    @Title : Python program to get the last part of a string before a specified character

"""
def get_last_part_before_char(string, char):
    """
    Description :
        This function is used to get the last part of a string before a specified character
    Parameters :
        string: The input string from which to extract the part
    return :
        str : The substring of the last part before the specified character
    """

    index = string.rfind(char)

    if index == -1:
        return string
    
    return string[:index]

def main():
    input_string = 'Deven_Gupta_Mumbai'
    char = '_'
    result = get_last_part_before_char(input_string, char)
    print(result) 

if __name__ == "__main__":
    main()