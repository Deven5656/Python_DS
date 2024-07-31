""" 
    @Author: Deven Gupta
    @Date: 29-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 29-07-2024
    @Title : Python program to find the repeated items of a tuple

"""
def repeated_element(tup):
    """
        Description :
            This function is used to find the repeated items of a tuple
        Parameters :
            tup : input tuple
        return :
            list : list having repeated number
     """
    repeated_element=[]
    for index in range(len(tup)):
        if tup[index] in tup[:index] + tup[index+1:] and tup[index] not in repeated_element:
            repeated_element.append(tup[index])

    return repeated_element


def main():
     input_tuple=(1,2,2,3,3,4,5,5,6)
     print(repeated_element(input_tuple))
if __name__ == "__main__":
    main()
