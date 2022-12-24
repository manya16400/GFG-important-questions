"""
Given a sorted array of positive integers. Your task is to rearrange the array elements alternatively i.e first element should be max value, second should be min value, third should be second max, fourth should be second min and so on.

Input:
n = 6
arr[] = {1,2,3,4,5,6}
Output: 6 1 5 2 4 3
Explanation: Max element = 6, min = 1, 
second max = 5, second min = 2, and 
so on... Modified array is : 6 1 5 2 4 3.

"""

#Function to rearrange  the array elements alternately.
def rearrange(self,arr, n): 
    ##Your code here

    res = [0]*n
    i = 0
    j = n-1

    tmp = 0

    while tmp<n:
        if tmp%2==0:
            res[tmp] = arr[j]
            j -= 1

        else:
            res[tmp] = arr[i]
            i += 1

        tmp += 1

    arr[::] = res
