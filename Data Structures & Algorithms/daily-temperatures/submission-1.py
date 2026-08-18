class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        s = []

        for i in range(n - 1, -1, -1):
            while s and temperatures[s[-1]] <= temperatures[i]:
                s.pop()
            if s:
                ans[i] = s[-1] - i
            
            s.append(i)
        
        return ans
