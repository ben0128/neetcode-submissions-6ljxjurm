class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        while left < right:
            tempSum = numbers[left]+numbers[right]
            if tempSum > target:
                right -= 1
            elif tempSum < target:
                left += 1
            else:
                return [left+1, right+1]
        


        # need add 1 to answer(1-indexed)

