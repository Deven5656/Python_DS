"""
    @Author: Deven Gupta
    @Date: 29-07-2024 
    @Last Modified by: Deven Gupta
    @Last Modified time: 29-07-2024 
    @Title: Python program to generate all permutations of a list in Python

"""

def permutation_of_list(lst):
    """
    Description: 
        This function is used to gives permutations of the given list
    Parameters:
        lst: list containing numbers 
    Return:
        none
    """
    for start in range(len(lst)):
        for end in range(start, len(lst)+1):
            if start < end:
                print(lst[start:end])


def main():
    input_list=[1,2,3,4,5]
    permutation_of_list(input_list)

if __name__ == "__main__":
    main()