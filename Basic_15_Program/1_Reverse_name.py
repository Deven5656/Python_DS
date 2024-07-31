""" 
@Author: Deven Gupta
    @Date: 26-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 26-07-2024
    @Title : Python program to print the name as (lastname firstname)
    
"""

def reverse_name(fname,lname):
    """
        Description :
            This function is used to fprint the as last name then first name
        Parameters :
            fname(string): user first name
            lname(string): user last name
        return :
            string
            
    """
    
    return f"{lname} {fname}"

def main():
   first_name=input("Enter the first name : ")
   last_name=input("Enter the last name : ")
   print(reverse_name(first_name,last_name))

if __name__ == "__main__":
    main()