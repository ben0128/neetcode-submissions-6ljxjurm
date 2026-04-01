class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)

        def backtrack(path, used):
            if len(path) == n:
                result.append(path[:])
                return

            for num in nums:
                if num not in used:
                    used.add(num)
                    path.append(num)
                    backtrack(path, used)
                    used.discard(num)
                    path.pop()

        backtrack([], set())

        return result


