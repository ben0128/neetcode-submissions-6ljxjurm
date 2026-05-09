class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        visited = defaultdict(int)
        visited[0] = 1
        n = len(nums)
        preflix = [0] * (n+1)
        count = 0
        
        for i in range(n):
            preflix[i+1] = preflix[i]+nums[i]
            count += visited[preflix[i+1] - k]
            visited[preflix[i+1]] += 1
        return count