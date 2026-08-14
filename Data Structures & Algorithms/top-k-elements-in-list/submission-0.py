from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        print(counts.most_common(k))
        final = []
        for num in counts.most_common(k):
            final.append(num[0])
        return final