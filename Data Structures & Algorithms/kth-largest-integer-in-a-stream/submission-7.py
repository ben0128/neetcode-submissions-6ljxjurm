class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        if len(nums) > k:
            self.sortLi = sorted(nums)[len(nums)-k:]
        else:
            self.sortLi = sorted(nums)
        self.k = k

    def add(self, val: int) -> int:
        left, right = 0, len(self.sortLi)
        while left < right:
            mid = left + (right-left)//2
            if self.sortLi[mid] < val:
                left = mid + 1
            else:
                right = mid
        self.sortLi.insert(left, val)
        return self.sortLi[len(self.sortLi)-self.k]