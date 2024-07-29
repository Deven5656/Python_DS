""" 
    @Author: Deven Gupta
    @Date: 26-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 26-07-2024
    @Title : Python program to find the length of string

"""

def check_len(string):
    """
        Description :
            This function is used to find the length of string
        Parameters :
            string: string words
        return :
            int : count of char in string
     """
    count=0
    for _ in string:
        count+=1
    return count


def main():

    string=input("Enter a string : ")
    print(f"length using inbuilt function is {len(string)}")
    print(f"length using user-defined function {check_len(string)}")


if __name__ == "__main__":
    main()
