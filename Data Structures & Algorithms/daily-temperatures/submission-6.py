class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = [] # [idx]
        # step1 foreach enumerate(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                popI = stack.pop()
                ans[popI] = i - popI
            
            stack.append(i)
        return ans

        # stack = [1,3 ,4 ,]
        # ans = [1, 0, 1, 0, 0, 0, 0]