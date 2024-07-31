""" 
    @Author: Deven Gupta
    @Date: 27-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 27-07-2024
    @Title :Python program to count occurrences of a substring in a string

"""
def count_occurrences(string, substring):
    """
    Description :
        This function is used to count occurrences of a substring in a string
    Parameters :
        string: The input string
        substring: substring which has to be checked
    return :
        int: count of substring
    """
    count = 0
    s_len = len(string)
    sub_len = len(substring)
    
    for i in range(s_len - sub_len + 1):

        if string[i:i + sub_len] == substring:
            count += 1
    
    return count

def main():
    string = "max is max not in max"
    substring = "max"
    count = count_occurrences(string, substring)
    print(f"The substring occurs {count} times in the string.")
    
if __name__ == "__main__":
    main()
   
