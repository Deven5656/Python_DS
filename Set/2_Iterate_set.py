""" 
    @Author: Deven Gupta
    @Date: 30-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 30-07-2024
    @Title : Python program to iteration over sets

"""
def iterate_set(input_set):
    """
        Description :
            This function is used to iterate over set
        Parameters :
            input_set: set containing numbers
        return :
            none
    """
    for item in input_set:
        print(item)
    
   
def main():
    input_set ={1,2,3,4,5}
    iterate_set(input_set)

if __name__ == "__main__":
    main()
