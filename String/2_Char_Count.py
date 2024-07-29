""" 
    @Author: Deven Gupta
    @Date: 26-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 26-07-2024
    @Title : Python program to count the number of characters (character frequency) in a string.

"""
def count_characters(string):
    """
        Description :
            This function is used to Count the frequency of each character in a string.
        Parameters :
            string: The input string whose characters' frequencies are to be counted.
        return :
            dict : A dictionary where keys are characters and values are their frequencies.
     """
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count
def main():
    sample_string = input("Enter the string : ")
    result = count_characters(sample_string)
    print(result)

if __name__ == "__main__":
    main()
