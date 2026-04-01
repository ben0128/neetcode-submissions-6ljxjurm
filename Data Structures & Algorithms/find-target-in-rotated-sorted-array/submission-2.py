class Solution:
    def search(self, nums: List[int], target: int) -> int:
        m = len(nums)
        l, r = 0, m-1
        while l < r:
            mid = l + (r-l) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        start = l
        global_min, global_max = nums[start], max(nums[start-1], nums[-1])
        if target > global_max or target < global_min:
            return -1

        l, r = -1, -1
        if nums[start] <= target <= nums[-1]:
            l, r = start, m-1
        else:
            l, r = 0, start-1
        
        while l < r:
            mid = l + (r-l)//2
            if nums[mid] < target:
                l = mid+1
            else:
                r = mid
        return l if nums[l] == target else -1
