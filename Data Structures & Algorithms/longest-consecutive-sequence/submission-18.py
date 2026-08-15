class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums)
        max_count = 0

        for num in nset:
            if num - 1 not in nset:
                current = num
                count = 1

                while current + 1 in nset:
                    current += 1
                    count += 1
                
                max_count = max(max_count, count)
        
        return max_count