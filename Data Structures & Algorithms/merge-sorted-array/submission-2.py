class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums2:
            return 
        heapq.heapify(nums2)

        for i in range(len(nums1)):
            if m > i and nums2[0] < nums1[i]:
                temp = heapq.heapreplace(nums2, nums1[i])
                nums1[i] = temp
            elif m <= i:
                temp = heapq.heappop(nums2)
                nums1[i] = temp