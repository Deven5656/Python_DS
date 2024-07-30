""" 
    @Author: Deven Gupta
    @Date: 29-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 29-07-2024
    @Title : Python program to find the list of words that are longer than n from a
             given list of words.


"""
def n_longer_word(lst,n):
    """
    Description :
        This function is used to find the list of words that are longer than n
    Parameters :
        lst : input List
        n  : length which has to be checked 
    return :
        list : containing string longer than n length
    """
    list_nlonger=[]

    for element in lst:
        if len(element) > n :
            list_nlonger.append(element)
    
    return list_nlonger


def main():
    input_list=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    number=int(input("Enter the length : "))
    print(n_longer_word(input_list,number)) 

if __name__ == "__main__":
    main()