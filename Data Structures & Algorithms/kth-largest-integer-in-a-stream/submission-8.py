class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        if len(nums) > k:
            self.sortLi = sorted(nums)[len(nums)-k:]
        else:
            self.sortLi = sorted(nums)
        self.sortLi.reverse()
        self.k = k

    def add(self, val: int) -> int:
        self.sortLi.append(val)
        self.sortLi.sort()
        self.sortLi.reverse()
        if len(self.sortLi) > self.k:
            self.sortLi.pop()
        return self.sortLi[self.k-1]