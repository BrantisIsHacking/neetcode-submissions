class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        sum1 = 0
        i = 0

        for j in range(len(gas)):
            sum1 += gas[j] - cost[j]
            if sum1 < 0:
                sum1 = 0
                i = j + 1
        return i