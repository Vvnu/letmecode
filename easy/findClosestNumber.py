# 2239. Find Closest Number to Zero
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an integer array nums of size n, return the number with the value closest to 0 in nums. If there are multiple answers, return the number with the largest value.

 

# Example 1:

# Input: nums = [-4,-2,1,4,8]
# Output: 1
# Explanation:
# The distance from -4 to 0 is |-4| = 4.
# The distance from -2 to 0 is |-2| = 2.
# The distance from 1 to 0 is |1| = 1.
# The distance from 4 to 0 is |4| = 4.
# The distance from 8 to 0 is |8| = 8.
# Thus, the closest number to 0 in the array is 1.
# Example 2:

# Input: nums = [2,-1,1]
# Output: 1
# Explanation: 1 and -1 are both the closest numbers to 0, so 1 being larger is returned.
 
class Solution(object):
    def findClosestNumber(self,nums):
        """
            :type nums: List[int]
            :rtype: int
            """
        #to start from the first element
        closet =nums[0]
        for num in nums:
            #to check if the absolute value of the number is less than the closest value if yes update the closest value
            if abs(num)< abs(closet):
                closet = num
            #if the absolute value is same then check for the greater value and update the closest value
            elif abs(num) == closet and num > closet:
                closet =num
        return closet
