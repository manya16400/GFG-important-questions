"""
Given an array arr of N integers, write a function that returns true if there is a triplet (a, b, c) that satisfies a2 + b2 = c2, otherwise false.

Input:
N = 5
Arr[] = {3, 2, 4, 6, 5}
Output: Yes
Explanation: a=3, b=4, and c=5 forms a
pythagorean triplet.

"""

def checkTriplet(self,arr, n):
  for i in range(n):
      arr[i] = arr[i] * arr[i]

  arr.sort()

  for i in range(n - 1, 1, -1):
      s = set()
      for j in range(i - 1, -1, -1):
          if (arr[i] - arr[j]) in s:
              return True
          s.add(arr[j])
  return False
