""" 
    @Author: Deven Gupta
    @Date: 26-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 26-07-2024
    @Title : Python program to print the documents (syntax, description etc.) of Python built-in function.
    
"""

def print_function_docs(func):
    """
        Description :
            This function is used get the name and documents of Python built-in function.
        Parameters :
            func :inbuilt function name
        return :
            tuple: which contain name and description of function
            
    """ 
    func_name = func.__name__
    func_docstring = func.__doc__

    return func_name,func_docstring

def main():
    name,document =print_function_docs(abs)

    print(f"Documentation for {name}():")
    print(document)

if __name__ == "__main__":
    main()