class Solution:
    def maxArea(self, height: List[int]) -> int:
        # left, right = 0, len(height) - 1
        # max_water = 0

        # while left < right:
        #     width = right - left
        #     current_water = min(height[left], height[right]) * width
        #     max_water = max(max_water, current_water)

        #     if height[left] < height[right]:
        #         left += 1
        #     else:
        #         right -= 1

        # return max_water
        area_arr = []
        for i in range(len(height)):
            for j in range(i,len(height)):
                area = min(height[i], height[j]) * (j-i)
                area_arr.append(area)

        area_arr.sort()
        return area_arr[-1]
