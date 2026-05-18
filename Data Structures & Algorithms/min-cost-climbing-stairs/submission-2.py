class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        steps = [float('inf')] * n
        steps[0], steps[1] = cost[0], cost[1]
        
        for idx in range(2, n):
            steps[idx] = cost[idx] + min(steps[idx-1], steps[idx-2])
        return min(steps[-1], steps[-2])

    # m = float('inf')
    # cost = [1,2] => 1
    # cost = [1, 2, 3] => 2
    # cost = [1,2,1,2,1,1,1]
    # steps= [1,2,2,4,3,4,4] => 4

    # return min(steps[-1], steps[-2])