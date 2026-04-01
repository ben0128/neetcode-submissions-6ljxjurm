class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        print(freq)
        freqList = []
        for key, value in freq.items():
            heapq.heappush(freqList, (-value, key))
        ans = []
        for _ in range(k):
            popEl = heapq.heappop(freqList)
            ans.append(popEl[1])
        return ans 
        

        






        