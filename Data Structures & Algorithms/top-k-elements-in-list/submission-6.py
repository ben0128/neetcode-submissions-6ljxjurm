class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {};
        for num in nums:
            dic[num] = dic.get(num, 0) + 1;
        freq = [[] for num in range(len(nums)+1)]
        for key, value in dic.items():
            freq[value].append(key);
        res = [];
        for idx in range(len(freq)-1, 0, -1):
            if len(freq[idx]) > 0:
                for item in freq[idx]:
                    res.append(item);
            if (len(res) == k):
                return res;






        