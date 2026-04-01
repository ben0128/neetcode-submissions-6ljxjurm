import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = k -1

        def quickselect(l , r):
            p = l
            pivotIdx = random.randint(l, r)
            nums[pivotIdx], nums[r] = nums[r], nums[pivotIdx]
            for idx in range(l, r):
                if nums[idx] > nums[r]:
                    nums[idx], nums[p] = nums[p], nums[idx]
                    p += 1
            print(pivotIdx)
            nums[p], nums[r] = nums[r], nums[p]
            print(nums)
            if p < k:
                return quickselect(p+1, r)
            elif p > k:
                return quickselect(l, p-1)
            else:
                return nums[p]

        return quickselect(0, len(nums)-1)