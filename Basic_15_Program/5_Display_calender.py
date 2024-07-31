""" 
    @Author: Deven Gupta
    @Date: 26-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 26-07-2024
    @Title : Python program to print the calendar of a given month and year.
    
"""

import calendar

def display_calender(month,year):
    """
        Description :
            This function is used get full calender of particular month and year
        Parameters :
            month: number of month form 1-12(jan to dec)
            year:  number of year in 4 digit (eg. 2004)
        return :
            str: full calender of that month in year
            
    """
    full_calender= calendar.month(year, month)

    return full_calender


def main():
    month = int(input("Enter the month (1-12): "))
    year = int(input("Enter the year (Ex. 2024): "))
    print("\n",display_calender(month,year))


if __name__ == "__main__":
    main()