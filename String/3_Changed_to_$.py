""" 
    @Author: Deven Gupta
    @Date: 26-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 26-07-2024
    @Title : Python program to get a string from a given string where all occurrences of its
             first char have been changed to '$', except the first char itself.

"""
def replace_first_char(string):
    """
    Description :
        This function is used to replace all occurrences of the first character in the string with '$'
    Parameters :
        string: The input string to be modified
    return :
        str : The modified string with specified replacements
    """
 
    first_char = string[0]  
    modified_string = first_char + string[1:].replace(first_char, '$')

    return modified_string

def main():
    sample_string = input("Enter the string : ")
    result = replace_first_char(sample_string)
    print(result)

if __name__ == "__main__":
    main()
