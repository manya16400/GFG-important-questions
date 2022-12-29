"""
Given a string S, find the longest palindromic substring in S. Substring of string S: S[ i . . . . j ] where 0 ≤ i ≤ j < len(S). Palindrome string: A string which reads the same backwards. More formally, S is palindrome if reverse(S) = S. Incase of conflict, return the substring which occurs first ( with the least starting index).


Input:
S = "aaaabbaa"
Output: aabbaa
Explanation: The longest Palindromic
substring is "aabbaa".

"""

def longestPalin(self, s):
  # code here

  if len(s)==1:
      return s

  for i in range(len(s),0,-1):
      for j in range(len(s)-i+1):
          x = s[j:i+j]
          if x==x[::-1]:
              return x
