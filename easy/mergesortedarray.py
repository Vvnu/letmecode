#merge two sorted array in m+n time and O(1) space     

# (simple trick)   = 
# nums1[m:] = nums2      ---------> this line copies nums2 into the empty space of nums1 which we get from the slicing the zeroes
# nums1.sort() ---> this line sorts the nums1 array which now contains all the elements of both arrays 

#  but the time compelxity is (m+n)log(m+n) due to the sorting   but benificial when have to do without extra space



class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1   # last valid element in nums1
        j = n - 1   # last element in nums2
        k = m + n - 1   # last position in nums1

        # merge from the back
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:    # compare and place the larger element at the end
                nums1[k] = nums1[i]      # place the larger element at the end
                i -= 1
            else:
                nums1[k] = nums2[j]         # place the larger element at the end
                j -= 1
            k -= 1

        # copy remaining nums2 elements (if any)
        while j >= 0:                        # if nums1 is exhausted but nums2 still has elements
            nums1[k] = nums2[j]               # copy remaining elements from nums2  
            j -= 1
            k -= 1
        return 
 

