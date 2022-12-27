"""
Given two sorted arrays arr1[] and arr2[] of sizes n and m in non-decreasing order. Merge them in sorted order without using any extra space. 


Input: 
n = 4, arr1[] = [1 3 5 7] 
m = 5, arr2[] = [0 2 6 8 9]

Output: 
arr1[] = [0 1 2 3]
arr2[] = [5 6 7 8 9]

Explanation:
After merging the two 
non-decreasing arrays, we get, 
0 1 2 3 5 6 7 8 9.

"""

#Function to merge the arrays.
def merge(self,arr1,arr2,n,m):

    #code here
    i = 0
    j = 0
    k = n - 1

    while (i <= k and j < m):
        if (arr1[i] < arr2[j]):
            i += 1
        else:
            temp = arr2[j]
            arr2[j] = arr1[k]
            arr1[k] = temp
            j += 1
            k -= 1

    arr1.sort()
    arr2.sort()

    return arr1+arr2
