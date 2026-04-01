class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        curr = 0
        res =  0
        for idx in range(len(gas)):
            curr += gas[idx]
            curr -= cost[idx]

            if curr < 0:
                res = idx + 1
                curr = 0
        return res
            