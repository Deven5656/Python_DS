"""
    @Author: Deven Gupta
    @Date: 29-07-2024 
    @Last Modified by: Deven Gupta
    @Last Modified time: 29-07-2024 
    @Title: Python program to split a list based on first character of word.

"""

def split_by_char(lst):
    """
    Description: 
        This function is used to split a list based on first character of word.
    Parameters:
        lst: list containing string
    Return:
        dict
    """
    result={}

    for element in lst:
        if element:
            first_char=element[0].lower()
            if first_char in result:
                result[first_char].append(element)
            else:
                result[first_char]=[element]
    return result
        


def main():
    input_list=["Deven","dev","prayag","prakash","shivraj","shivtej"]
    print(split_by_char(input_list))

if __name__ == "__main__":
    main()