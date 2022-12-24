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
