class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for n in asteroids:
            if n > 0:
                stack.append(n)
                continue
                
            while stack and stack[-1] > 0 and stack[-1] < abs(n):
                stack.pop()
            if stack and stack[-1] > 0:
                if stack[-1] == abs(n):
                    stack.pop()
                    continue
                elif stack[-1] > abs(n):
                    continue
            stack.append(n)

        return stack


                
