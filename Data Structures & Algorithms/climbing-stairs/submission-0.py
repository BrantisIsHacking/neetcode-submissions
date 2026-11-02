class Solution:
    def climbStairs(self, n: int) -> int:
        phi = (1 + math.sqrt(5)) / 2
        psi = (1 - math.sqrt(5)) / 2
        n += 1
        return round((phi**n - psi**n) / math.sqrt(5))