#majority Element Problem
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
# Example 1:
# Input: nums = [3,2,3]     
# Output: 3
# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        element = None

        for num in nums:
            if count == 0:
                element = num   # choose new candidate
            if num == element:
                count += 1
            else:
                count -= 1

        return element
# The Boyer-Moore Voting Algorithm is used here to find the majority element in linear time and constant space.
