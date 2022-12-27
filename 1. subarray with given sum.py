"""
Given an unsorted array A of size N that contains only non-negative integers, find a continuous sub-array which adds to a given number S and return the left and right index(1-based indexing) of that subarray.

Input:
N = 5, S = 12
A[] = {1,2,3,7,5}
Output: 2 4
Explanation: The sum of elements 
from 2nd position to 4th position 
is 12.

"""


#function to find a continuous sub-array which adds upto a given number

def subArraySum(arr, n, s): 
       #Write your code here
       
       l = 0 
       r = 0
       
       ans = 0
       
       found = False
       
       while r<n:
           curr_sum = ans + arr[r]
           if curr_sum < s:
               ans += arr[r]
               r += 1
           elif curr_sum == s:
               return [l+1,r+1]
               break
               
           else :
               ans -= arr[l]
               l += 1
               
       return [-1]
