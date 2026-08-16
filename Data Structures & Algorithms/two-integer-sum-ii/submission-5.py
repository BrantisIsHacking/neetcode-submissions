class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        h = {}

        for i, num in enumerate(numbers):
            complement = target - num
            if complement in h:
                return [h[complement] + 1, i + 1]
            h[num] = i
        
        return []