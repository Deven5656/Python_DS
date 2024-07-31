""" 
    @Author: Deven Gupta
    @Date: 26-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 26-07-2024
    @Title : Python program to call an external command in Python.

"""
import subprocess

def call_external_command(command):
    """
        Description :
            This function is used to call an external command in Python
        Parameters :
            command (list): The command to execute as a list of strings.
        return :
            subprocess.CompletedProcess
    """

    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    return result.stdout

def main():
    # Check the operating system
    command = ['dir']  
    print("Result:",call_external_command(command))

if __name__ == "__main__":
    main()