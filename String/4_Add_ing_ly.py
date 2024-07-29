""" 
    @Author: Deven Gupta
    @Date: 26-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 26-07-2024
    @Title : Python program to add 'ing' at the end of a given string (length should be atleast 3). 
             If the given string already ends with 'ing' then add 'ly' instead. If the string length of the
             given string is less than 3, leave it unchanged.
"""
def modify_string(string):
    """
    Description :
        This function is used to modify the string based on its length and suffix.
    Parameters :
        string: The input string to be modified
    return :
        str : The modified string according to condition
    """
    if len(string) < 3:
        return string
    if string.endswith('ing'):
        return string + 'ly'
    else:
        return string + 'ing' 

def main():
    sample_string = input("Enter the string : ")
    result = modify_string(sample_string)
    print(result)

if __name__ == "__main__":
    main()

