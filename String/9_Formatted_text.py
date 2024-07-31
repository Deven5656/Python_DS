""" 
    @Author: Deven Gupta
    @Date: 27-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 27-07-2024
    @Title : Python program to display formatted text (width=50) as output.

"""

def format_txt(string):
    """
    Description :
        This function is used to print the string after width = 50
    Parameters :
        string: The input string
    return :
        none
    """
    for i in range(len(string)):
        if i % 50 == 0:
            print("")
        else:
            print(string[i],end="")

def main():
    string = "*"*200+"#"*20
    format_txt(string)
  
if __name__ == "__main__":
    main()
   