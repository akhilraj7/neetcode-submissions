class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof_arr = []
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                profit = prices[j] - prices[i]
                if profit >= 0:
                    prof_arr.append(profit)

        prof_arr.sort()
        return prof_arr[-1]
