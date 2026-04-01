class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for idx, num in enumerate(numbers):
            diff = target - numbers[idx]
            right = len(numbers)-1
            left = idx+1
            while left <= right:
                mid = left + (right-left) // 2
                if (numbers[mid] == diff):
                    return [idx+1, mid+1]
                elif numbers[mid] < diff:
                    left = mid+1
                else: 
                    right = mid-1

