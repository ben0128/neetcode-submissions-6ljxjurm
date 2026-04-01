class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1: 
            return len(nums)
        
        dic = dict()
        for num in nums:
            dic[num] = True
        print(dic)
        maxLen = 0
        temp = 0

        for num in dic.keys():
            if num in dic and dic[num] == True:
                temp += 1
                left = num-1
                right = num+1
                while left in dic and dic[left] == True:
                    temp += 1
                    dic[left] = False
                    left -= 1
                while right in dic and dic[right] == True:
                    temp += 1
                    dic[right] = False
                    right += 1
                maxLen = max(maxLen, temp)
            temp = 0
        return maxLen

        
                

