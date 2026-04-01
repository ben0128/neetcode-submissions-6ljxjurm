class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = k -1

        def quickselect(l , r):
            p = l
            pivot = nums[r]
            for idx in range(l, r):
                if nums[idx] > pivot:
                    nums[idx], nums[p] = nums[p], nums[idx]
                    p += 1
            
            nums[p], nums[r] = nums[r], nums[p]
            print(nums, p, pivot)
            if p < k:
                return quickselect(p+1, r)
            elif p > k:
                return quickselect(l, p-1)
            else:
                return nums[p]

        return quickselect(0, len(nums)-1)