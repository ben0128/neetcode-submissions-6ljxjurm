class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1: init hashMap {[number]: [index]}
        numMap = {}
        # 2: foreach nums
        for idx, num in enumerate(nums):
            need = target - num
            if need in numMap:
                return [numMap[need], idx]
            else:
                numMap[num] = idx