class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        record = defaultdict()

        for idx, number in enumerate(numbers):
            tempTarget = target - number
            if tempTarget in record:
                return [record[tempTarget]+1, idx+1]
            else:
                record[number] = idx

        # need add 1 to answer(1-indexed)

