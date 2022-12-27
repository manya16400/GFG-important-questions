"""
Given an array A of n positive numbers. The task is to find the first Equilibrium Point in an array. 
Equilibrium Point in an array is a position such that the sum of elements before it is equal to the sum of elements after it.

Input: 
n = 5 
A[] = {1,3,5,2,2} 
Output: 3 
Explanation:  
equilibrium point is at position 3 
as elements before it (1+3) = 
elements after it (2+2). 

"""

def equilibriumPoint(self,A, N):
  # Your code here

  if N==1:
      return 1

  rs,ls = sum(A),0

  for i in range(N):

      rs-=A[i]

      if ls==rs:

          return i+1

      ls+=A[i]

  return -1
