class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        freqList = [[] for _ in range(len(freq.keys())+1)]
        for num, times in freq.items():
            freqList[times-1].append(num)
        ans = []
        print(freqList)
        for item in freqList[::-1]:
            if len(item) > 0:
                for ansEl in item:
                    ans.append(ansEl)
                if k == len(ans):
                    return ans
                


        
        

        






        