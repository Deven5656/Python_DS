""" 
    @Author: Deven Gupta
    @Date: 26-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 26-07-2024
    @Title : Python program that takes input from the user and displays that input back in upper and lower cases.
"""
def to_upper_lower(string):
    """
    Description :
        This function is used to displays that input back in upper and lower cases
    Parameters :
        string: The input string 
    return :
        str : string in uppercase and lowercase
    """
    upper_case =string.upper()
    lower_case =string.lower()
    
    return upper_case,lower_case

def main():
    sample_string = input("Enter the string : ")
    string_to_upper,string_to_lower = to_upper_lower(sample_string)
    print(f"String to uppercase is {string_to_upper} and to lowercase is {string_to_lower}")

if __name__ == "__main__":
    main()