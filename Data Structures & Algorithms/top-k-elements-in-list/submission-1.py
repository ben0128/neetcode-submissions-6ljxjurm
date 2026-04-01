class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {};
        for num in nums:
            dic[num] = dic.setdefault(num, 0) + 1;
        li = sorted(dic.items(), key=lambda item: item[1] , reverse=True)
        return [item[0] for item in li[:k]  ]
        