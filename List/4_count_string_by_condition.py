""" 
    @Author: Deven Gupta
    @Date: 29-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 29-07-2024
    @Title : Python program to count the number of strings where the string length 
             is 2 or more and the first and last character are same from a given list of strings.

"""
def count_string(lst):
    """
    Description :
        This function is used to count the number of strings
    Parameters :
        lst : input List of string
    return :
        int : count the number of strings
    """
    count = 0
    for element in lst:
        if len(element) >= 2 and element[0] == element[-1]:
            count+=1
    return count

def main():
    input_list=['abc', 'xyz', 'aba', '1221','bb']
    print(count_string(input_list)) 

if __name__ == "__main__":
    main()