"""
Given an array A of positive integers. Your task is to find the leaders in the array. An element of array is leader if it is greater than or equal to all the elements to its right side. The rightmost element is always a leader. 

Input:
n = 6
A[] = {16,17,4,3,5,2}
Output: 17 5 2
Explanation: The first leader is 17 
as it is greater than all the elements
to its right.  Similarly, the next 
leader is 5. The right most element 
is always a leader so it is also 
included.

"""

def leaders(self, A, N):
  #Code here
  max_ = 0
  res = []

  for i in range(N-1,-1,-1):
      max_ = max(max_,A[i])
      if max_ <= A[i]:
          res.append(A[i])

  return res[::-1]
