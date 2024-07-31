""" 
    @Author: Deven Gupta
    @Date: 30-07-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 30-07-2024
    @Title : Python program to concatenate dictionaries

"""

def concatenate_dict(dic1,dic2,dic3):
    """
        Description :
            This function is used to concatenate dictionaries
        Parameters :
            dic1: 1st input dictionary
            dic2: 2nd input dictionary
            dic3: 3rd input dictionary
        return :
            dict : concatenated dictionary
     """
    # dic1.update(dic2)
    # dic1.update(dic3)

    for key,value in dic2.items():
        dic1[key]=value
    for key,value in dic3.items():
        dic1[key]=value
    return dic1

def main():

    dic1={1:10, 2:20}
    dic2={3:30, 4:40}
    dic3={5:50,6:60}
    print(concatenate_dict(dic1,dic2,dic3))


if __name__ == "__main__":
    main()
