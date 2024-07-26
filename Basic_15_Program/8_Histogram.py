""" 
    @Author: Deven Gupta
    @Date: 26-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 26-07-2024
    @Title : Python program to create a histogram from a given list of integers.
    
"""
def histogram(items):
    """
        Description :
            This function is used to print the histogram from a given list of integers.
        Parameters :
            items: list of integers
        return :
            none    
    """
    for n in items:
        output = '' 
        times = n     
        
        # Use a while loop to append '*' to the output string 'times' number of times.
        while times > 0:
            output += '*'
            times = times - 1

        print(output)


def main():
    items=[2, 3, 6, 5]
    histogram(items)


if __name__ == "__main__":
    main()