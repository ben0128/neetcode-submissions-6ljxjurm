class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = -1
        numSet = defaultdict(int)
        for i, num in enumerate(nums):
            if num not in numSet:
                numSet[num] = i
            else:
                if i - numSet[num] <= k:
                    return True
                else:
                    numSet[num] = i
        return False

