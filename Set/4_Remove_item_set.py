""" 
    @Author: Deven Gupta
    @Date: 30-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 30-07-2024
    @Title : Python program to remove item(s) from set

"""
def remove_item(input_set,n):
    """
        Description :
            This function is used to remove item(s) from set
        Parameters :
            input_set : set with itmes
            n : number od items to be remove
        return :
            set : after removing items
    """
    
    for _ in range(n):
       input_set.pop()
    
    return input_set
def main():
    input_set ={1,2,3,4,5}
    number=int(input("number of items remove : "))
    print(remove_item(input_set,number))

if __name__ == "__main__":
    main()
