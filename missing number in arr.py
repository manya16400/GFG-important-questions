"""

Given an array arr[] of size N-1 with integers in the range of [1, N], the task is to find the missing number from the first N integers.

Input: arr[] = {1, 2, 4, 6, 3, 7, 8}, N = 7
Output: 5
Explanation: The missing number between 1 to 8 is 5

Input: arr[] = {1, 2, 3, 5}, N = 5
Output: 4
Explanation: The missing number between 1 to 5 is 4

"""

def MissingNumber(self,array,n):
  return n*(n+1)//2 - sum(array)

