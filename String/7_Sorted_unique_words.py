""" 
    @Author: Deven Gupta
    @Date: 26-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 26-07-2024
    @Title : Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form

"""

def unique_sorted_words(input_string):
    """
    Description :
        This function is used to print the unique words in sorted order
    Parameters :
        input_string: A string containing comma-separated words. 
    return :
        set : set of sorted words
    """
    words = [word.strip() for word in input_string.split(',')]

    unique_words = set(words)

    sorted_unique_words = sorted(unique_words)

    return sorted_unique_words


def main():
    input_string = input("Enter the string separated with commas : ")
    print(', '.join(unique_sorted_words(input_string)))
    

if __name__ == "__main__":
    main()