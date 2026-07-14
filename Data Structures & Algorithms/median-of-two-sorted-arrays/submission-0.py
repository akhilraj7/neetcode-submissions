class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        new_arr = nums1 + nums2
        new_arr.sort()
        len_arr = len(new_arr)
        left, right = 0, len_arr
        mid = (left + right) // 2

        if len_arr == 0:
            return 0

        if len_arr % 2 == 0:
            med = (new_arr[mid] + new_arr[mid-1]) / 2
        else:
            med = new_arr[mid]

        return med
             
        # for i in range(len(new_arr)):