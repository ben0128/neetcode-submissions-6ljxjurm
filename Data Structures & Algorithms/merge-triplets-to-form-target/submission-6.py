class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # 利用bitwise
        ans = 0
        for triplet in triplets:
            if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                for i in range(3):
                    if triplet[i] == target[i]:
                        ans |= (1 << i)
                if ans == 7:
                    return True
        return False