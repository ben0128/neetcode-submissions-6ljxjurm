class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) // 2
        if sum(nums) % 2 != 0:
            return False
        
        memo = set([0, nums[0]])
        if target in memo:

            print('check1', memo, target)
            return True

        for idx in range(1, len(nums)):
            tmp = []
            for el in memo:
                tmp.append(el+nums[idx])
            memo.update(tmp)
            if target in memo:
                print('check2')
                return True
        print(memo)
        return False

