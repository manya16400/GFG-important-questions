"""

Given an array Arr[] of N integers. Find the contiguous sub-array(containing at least one number) which has the maximum sum and return its sum.

Input:
N = 5
Arr[] = {1,2,3,-2,5}
Output:
9
Explanation:
Max subarray sum is 9
of elements (1, 2, 3, -2, 5) which 
is a contiguous subarray.

"""

#Function to find the sum of contiguous subarray with maximum sum.
def maxSubArraySum(self,arr,N):
    ##Your code here

    curr_so_far = -8732678268
    curr_end = 0

    for i in arr:
        curr_end += i
        if curr_so_far < curr_end:
            curr_so_far = curr_end

        if curr_end < 0:
            curr_end = 0

    return curr_so_far
