class Solution:
    def findMin(self, nums: List[int]) -> int:
        def search(l: int, r: int) -> int:
            if nums[l] <= nums[r]:
                return nums[l]
            
            m = (l + r) // 2

            if nums[l] <= nums[m]:
                return search(m + 1, r)
            
            return search(l, m)
        
        return search(0, len(nums) - 1)