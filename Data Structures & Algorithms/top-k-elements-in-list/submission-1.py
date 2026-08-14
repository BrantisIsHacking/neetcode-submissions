from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        final = []
        for num in counts.most_common(k):
            final.append(num[0])
        return final