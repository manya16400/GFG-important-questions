"""

Given a string S. The task is to print all unique permutations of the given string in lexicographically sorted order.

Input: ABC
Output:
ABC ACB BAC BCA CAB CBA
Explanation:
Given string ABC has permutations in 6 
forms as ABC, ACB, BAC, BCA, CAB and CBA .

"""

def find_permutation(self, S):
  # Code here
  res = []

  def backtrack(a, l, r):

      if l == r:
          res.append(''.join(a))
      else:
          for i in range(l, r):
              a[l], a[i] = a[i], a[l]
              backtrack(a, l+1, r)
              a[l], a[i] = a[i], a[l]

  a = [i for i in S]
  backtrack(a,0,len(S))
  return sorted(list(set(res)))
