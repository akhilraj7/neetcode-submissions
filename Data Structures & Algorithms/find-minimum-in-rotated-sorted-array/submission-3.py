class Solution:
    def findMin(self, nums: List[int]) -> int:
        # for i in range(len(nums)):
        #     for j in range(1, len(nums)):
        #         if nums[i] > nums[j]:
        #             temp = nums[j]
        #             nums[j] = nums[i]
        #             nums[i] = temp
        # return nums[0]
        len_nums = len(nums)
        left = 0
        right = len_nums - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]
