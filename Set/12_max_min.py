""" 
    @Author: Deven Gupta
    @Date: 30-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 30-07-2024
    @Title :  Python program to find maximum and the minimum value in a set.
"""
def max_min(input_set):
    """
        Description :
            This function is used to find maximum and the minimum value in a set.
        Parameters :
            input_set : set with items
        return :
            tuple : having maximum and minimum
    """
    maxi=float('-Inf')  # negative infinite value
    mini=float('Inf')   # positive infinite value
    for item in input_set:
        if item > maxi :
            maxi = item
        if item < mini :
            mini = item

    return maxi,mini

    
def main():
    input_set ={1,2,3,4,55}
    maximum,minimum=max_min(input_set)
    print(f"The max value is {maximum} and min value is {minimum}")

if __name__ == "__main__":
    main()
