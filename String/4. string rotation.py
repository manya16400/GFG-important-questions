"""
Given two strings a and b. The task is to find if the string 'b' can be obtained by rotating another string 'a' by exactly 2 places.

Input:
a = amazon
b = azonam
Output: 1
Explanation: amazon can be rotated anti
clockwise by two places, which will make
it as azonam.

"""

#Function to check if a string can be obtained by rotating
#another string by exactly 2 places.
def isRotated(self,str1,str2):
    #code here

    n = len(str1)

    # 2 place rotation from start
    if str1[2:]+str1[:2] == str2:
        return 1
    
    # 2 place rotation from end
    if str1[-2:]+str1[:-2] == str2:
        return 1

    return 0
