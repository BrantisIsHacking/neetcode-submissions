class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, best = 0, 0
        for r in range(1, len(prices)):
            if prices[r] < prices[l]:
                l = r
            else:
                curr = prices[r]-prices[l]
                best = max(best, curr)
        return best