""" 
    @Author: Deven Gupta
    @Date: 30-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 30-07-2024
    @Title : Python program to print a dictionary in table format.

"""

def iterate_dict(dic1):
    """
        Description :
            This function is used to print a dictionary in table format.
        Parameters :
            dic1: input dictionary
        return :
            none
     """
    print(f"*"*27)
    for key,value in dic1.items():
        
        print(f"| {key:^10} | {value:^10} |")
        print(f"*"*27)
  
def main():

    dic1={1:10, 2:20, 3:30, 4:40, 5:50, 6:60}

    iterate_dict(dic1)


if __name__ == "__main__":
    main()
