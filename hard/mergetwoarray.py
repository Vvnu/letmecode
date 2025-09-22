class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3=nums1+nums2
        nums3.sort()
        l =len(nums3)

        if l %2 ==0:   # if the length of the merged array is even
            mid1= nums3[l//2]
            mid2=nums3[l//2-1]
            return (mid1+mid2) / 2.0   # return the average of the two middle elements as float

        else:          # if the length of the merged array is odd
            return float (nums3[l//2])   # return the middle element as float
        
