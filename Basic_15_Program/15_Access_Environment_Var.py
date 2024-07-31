""" 
    @Author: Deven Gupta
    @Date: 26-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 26-07-2024
    @Title : Python program to access environment variables.

"""
import os

def access_environment_variables(variable_name):
    """
        Description :
            This function is used to access environment variables.
        Parameters :
            variable_name (str): The name of the environment variable to be access.
        return :
            str : path to that variable
    """

    variable_value = os.getenv(variable_name)
    return variable_value

def main():
    variable_name = 'TEMP'
    variable_value = access_environment_variables(variable_name)
    print(f"{variable_name}: {variable_value}")


if __name__ == "__main__":
    main()