"""
Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.

"""

def sort012(self,arr,n):
        # code here
        
        cnt0 = 0
        cnt1 = 0
        cnt2 = 0
    
        # Count the number of 0s, 1s and 2s in the array
        for i in range(n):
            if arr[i] == 0:
                cnt0 += 1
    
            elif arr[i] == 1:
                cnt1 += 1
    
            elif arr[i] == 2:
                cnt2 += 1
                
        arr[::] = [0]*cnt0 + [1]*cnt1 + [2]*cnt2
        
        return arr
