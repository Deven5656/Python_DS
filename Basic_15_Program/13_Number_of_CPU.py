""" 
    @Author: Deven Gupta
    @Date: 26-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 26-07-2024
    @Title : Python program to find out the number of CPUs using.

"""
import os

def find_number_of_cpus():
    """
        Description :
            This function is used to find out the number of CPUs using.
        Parameters :
            none
        return :
            none
    """
   
    num_cpus = os.cpu_count()
    print(f"Number of CPUs: {num_cpus}")

def main():
    find_number_of_cpus()

if __name__ == "__main__":
    main()