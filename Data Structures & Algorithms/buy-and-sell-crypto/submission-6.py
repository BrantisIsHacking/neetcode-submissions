class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, best = 0, 0
        for r in range(1, len(prices)):
            if prices[r] < prices[l]:
                l = r
            else:
                best = max(best, prices[r]-prices[l])
        return best