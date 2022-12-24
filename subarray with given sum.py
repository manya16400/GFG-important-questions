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
