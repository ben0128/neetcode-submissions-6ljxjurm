class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = dict()
        for (idx,num) in enumerate(numbers):
            if target-num in dic:
                return [dic[target-num]+1, idx+1]
            else:
                dic[num] = idx