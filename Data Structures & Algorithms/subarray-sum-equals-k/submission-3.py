class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        visited = defaultdict(int)
        visited[0] = 1
        n = len(nums)
        preflix = 0
        count = 0
        
        for i in range(n):
            preflix += nums[i]
            count += visited[preflix - k]
            visited[preflix] += 1
        return count