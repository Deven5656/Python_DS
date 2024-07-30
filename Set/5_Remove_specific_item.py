""" 
    @Author: Deven Gupta
    @Date: 30-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 30-07-2024
    @Title : Python program to remove an item from a set if it is present in the set

"""
def remove_item(input_set,item):
    """
        Description :
            This function is used to remove an item from a set if it is present in the set
        Parameters :
            input_set : set with itmes
            item : item to be remove
        return :
            set : after removing items
    """
  
    if item in input_set :
        input_set.remove(item)
    
    return input_set
def main():
    input_set ={1,2,3,4,55}
    item_to_remove= 55
    print(remove_item(input_set,item_to_remove))

if __name__ == "__main__":
    main()
