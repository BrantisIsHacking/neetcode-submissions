class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()

        max_count = 1
        current_count = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            if nums[i] == nums[i - 1] + 1:
                current_count += 1
            else:
                max_count = max(max_count, current_count)
                current_count = 1
        return max(max_count, current_count)    
