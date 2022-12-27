"""
Given an array arr[] of positive integers of size N. Reverse every sub-array group of size K.

Input:
N = 5, K = 3
arr[] = {1,2,3,4,5}
Output: 3 2 1 5 4
Explanation: First group consists of elements
1, 2, 3. Second group consists of 4,5.

"""

def reverseInGroups(self, arr, N, K):
  # code here

  i = 0

  while i<N:
      l = i
      r = min(l+K-1,N-1)

      while l<=r:
          arr[l], arr[r] = arr[r], arr[l]
          l += 1
          r -= 1

      i += K

  return arr
