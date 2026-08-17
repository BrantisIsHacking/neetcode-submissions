class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
    
        bars = len(height)
        lmax = [0] * bars
        rmax = [0] * bars

        lmax[0] = height[0]
        for i in range(1, bars):
            lmax[i] = max(lmax[i - 1], height[i])
        
        rmax[-1] = height[-1]
        for i in range(bars - 2, -1, -1):
            rmax[i] = max(rmax[i + 1], height[i])

        total = 0
        for i in range(bars):
            level = min(lmax[i], rmax[i])
            total += level - height[i]
        
        return total