class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False

        need = total // k
        nums.sort(reverse=True)
        if nums[0] > need:
            return False
        n = len(nums)
        def backtracing(idx, buckets):
            if idx == n:
                return True
            
            seen = set()
            for j in range(k):
                if buckets[j] >= nums[idx] and buckets[j] not in seen:
                    buckets[j] -= nums[idx]
                    if backtracing(idx+1, buckets):
                        return True
                    buckets[j] += nums[idx]
                    seen.add(buckets[j])
                if buckets[j] == need:
                    break
            return False

        return backtracing(0, [need] * k)