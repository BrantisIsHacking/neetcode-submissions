
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero = 0
        for num in nums:
            if num != 0:
                prod *= num
            else:
                zero += 1

        l = []

        if zero > 1:
            for _ in nums:
                l.append(0)
        elif zero == 1:
            for num in nums:
                if num == 0:
                    l.append(prod)
                else:
                    l.append(0)        
        else:
            for num in nums:
                l.append(prod // num)

        return l