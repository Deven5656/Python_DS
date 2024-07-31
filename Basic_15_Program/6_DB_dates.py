""" 
    @Author: Deven Gupta
    @Date: 26-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 26-07-2024
    @Title : Python program to find the number of days between 2 dates
    
"""

import datetime as DT


def find_diff(date1,date2):
    """
        Description :
            This function is used to find the number of days between 2 dates
        Parameters :
            date1,date2: 2 date in format of (YYYY,MM,DD)
        return :
            datetime.timedelta     
    """
    date_difference = date2 - date1
    print(type(date_difference))

    return date_difference

def main():

    date1 = DT.datetime(2014, 7, 2)
    date2 = DT.datetime(2014, 7, 11)
    print(f"Number of days between {date1.date()} and {date2.date()}: {find_diff(date1,date2).days} days")


if __name__ == "__main__":
    main()