class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if target == nums[i]+nums[j]:
        #             return [i,j]

        diff_arr = {}

        for i,num in enumerate(nums):
            diff = target - num

            if diff in diff_arr:
                return [diff_arr[diff], i]

            else:
                diff_arr[num] = i
        return []
            