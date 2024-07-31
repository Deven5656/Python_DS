""" 
    @Author: Deven Gupta
    @Date: 26-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 26-07-2024
    @Title : Python function that takes a list of words and returns the length of the longest one.
"""
def longest_word_length(words):
    """
    Description :
        This function is used to find the length of the longest word in list.
    Parameters :
        words(list): List containing words(string)
    return :
        int : The length of the longest word in the list. If the list is empty, returns 0.
    """
    max_length = 0
    
    for word in words:
        if len(word) > max_length:
            max_length=len(word)
    
    return max_length

def main():
    words_list = ['Deven', 'om', 'devraj', 'priyanshu']
    print(longest_word_length(words_list)) 

if __name__ == "__main__":
    main()




