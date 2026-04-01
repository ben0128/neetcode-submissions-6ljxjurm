class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        ans = 0
        l, r = 0, len(people)-1
        while l <= r:
            if l == r:
                return ans+1
            if people[r]+people[l] <= limit:
                l += 1
            ans += 1
            r -= 1
        return ans
            
