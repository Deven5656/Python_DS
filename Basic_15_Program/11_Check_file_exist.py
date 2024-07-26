""" 
    @Author: Deven Gupta
    @Date: 26-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 26-07-2024
    @Title : Python program to check whether a file exists.

"""
import os

def check_file_exists(path):
    """
        Description :
            This function is used to check whether a file exists.
        Parameters :
            path (str): The path to the file.
        return :
            none
    """
    if os.path.isfile(path):
        print(f"The file '{path}' exists.")
    else:
        print(f"The file '{path}' does not exist.")

def main():
    file_path = 'C:/Users/Deven/Desktop/Python Basics/Python_DS/11_Check_file_exist.py'
    check_file_exists(file_path)

if __name__ == "__main__":
    main()