class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
            
        nums = sorted(list(set(nums)))
        max_count = 1
        count = 1

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]-1:
                count +=1
            else:
                count = 1
            max_count = max(max_count, count)
        return max_count