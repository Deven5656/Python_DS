""" 
    @Author: Deven Gupta
    @Date: 26-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 26-07-2024
    @Title : Python program to list all files in a directory in Python.

"""
import os

def list_files_in_directory(directory_path):
    """
        Description :
            This function is used to get all files in a directory in Python
        Parameters :
            directory_path (str): The path to the directory.
        return :
            list : contains all directory
    """
  
    files = os.listdir(directory_path)
    return files


def main():
    directory_path = 'C:/Users/Deven/Desktop/Python Basics//Python_DS'
    files = list_files_in_directory(directory_path)
    print(f"Files in '{directory_path}':")
    for file in files:
        print(file)

if __name__ == "__main__":
    main()