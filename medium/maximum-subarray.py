# 53. Maximum Subarray
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an integer array nums, find the subarray with the largest sum, and return its sum.

 

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum =nums[0]
        curr_sum=0
        for i in range(len(nums)):
            curr_sum+=nums[i]
            if(curr_sum > max_sum):
                max_sum = curr_sum
            if (curr_sum <= 0):
                curr_sum=0 

        return max_sum
      

