""" 
    @Author: Deven Gupta
    @Date: 26-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 26-07-2024
    @Title :Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2.

"""
def unique_colors(l1, l2):
    """
        Description :
            This function is used to find unique colors from the first list that are not in the second list.
        Parameters :
            l1 (set): The first set of colors.
            l2 (set): The second set of colors.
        return :
            set: A set of unique colors from the first list.
    """
    unique = {color for color in l1 if color not in l2}  #set comprehension
    return unique

def main():
    color_list_1 = set(["White", "Black", "Red"])  
    color_list_2 = set(["Red", "Green"]) 

    
    print("Unique color set is", unique_colors(color_list_1, color_list_2))

if __name__ == '__main__':
    main() 