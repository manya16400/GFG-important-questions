class Solution:
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
