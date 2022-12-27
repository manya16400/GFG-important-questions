"""
Given an array of distinct integers. The task is to count all the triplets such that sum of two elements equals the third element.

Input: 
N = 4 
arr[] = {1, 5, 3, 2}
Output: 2 
Explanation: There are 2 triplets:
 1 + 2 = 3 and 3 +2 = 5
 
 """

def countTriplet(self, arr, n):
	c = 0
	d = {}
    
    for i in range(n):
	d[arr[i]]=i

    for i in range(n-1):
	for j in range(i+1,n):
	     if arr[i]+arr[j] in d:
		     c+=1

    return c
