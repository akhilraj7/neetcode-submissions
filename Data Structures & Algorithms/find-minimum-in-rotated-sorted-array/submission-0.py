class Solution:
    def findMin(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if nums[i] > nums[j]:
                    temp = nums[j]
                    nums[j] = nums[i]
                    nums[i] = temp
        return nums[0]
