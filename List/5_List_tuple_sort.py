""" 
    @Author: Deven Gupta
    @Date: 29-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 29-07-2024
    @Title: Python program to get a list, sorted in increasing order by the last
            element in each tuple from a given list of non-empty tuples.

"""
def list_tuple_sort(lst):
    """
    Description :
        This function is used to sort list in increasing order by the last element in each tuple
    Parameters :
        lst : input List having tuples as elements
    return :
        list : sorted list
    """

    for i in range(len(lst)-1):
        for j in range(i,len(lst)):
            if lst[i][-1]>lst[j][-1]:
                lst[i],lst[j]=lst[j],lst[i]

    return lst
       

def main():
    input_list= [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    print(list_tuple_sort(input_list)) 

if __name__ == "__main__":
    main()