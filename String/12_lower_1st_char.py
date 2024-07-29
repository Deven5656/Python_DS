""" 
    @Author: Deven Gupta
    @Date: 27-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 27-07-2024
    @Title : Python program to lowercase first n characters in a string.
"""
def lower_char_instring(string,number):
    """
    Description :
        This function is used to lower the first n char of string.
    Parameters :
        string: the input string
        number: number of letter to convert in lowercase
    return :
        string : modified string
    """
    modified_string=''

    modified_string= string[:number].lower() + string[number:]
    
    return modified_string

def main():
    string="ABDSNCSDDAJKDJAJDJAJDJKAJDJIDOAJDKJAKD"
    number=int(input("Enter How many letters to lowercase"))
    print(lower_char_instring(string,number)) 

if __name__ == "__main__":
    main()
