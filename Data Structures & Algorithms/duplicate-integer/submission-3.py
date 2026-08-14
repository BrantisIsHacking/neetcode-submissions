class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #for i in range(len(nums)):
        #    for j in range(len(nums)-i-1):
        #        if nums[i] == nums[i+j+1]:
        #            return True
        #return False
        hashmap = {}

        for num in nums:
            if num in hashmap:
                return True
            hashmap[num] = True
        return False