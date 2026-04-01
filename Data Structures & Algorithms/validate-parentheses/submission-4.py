class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        
        hashMap = {
            "]": "[",
            ")": "(",
            "}": "{" 
        }

        stack = []

        for item in s:
            if item not in hashMap:
                stack.append(item)
            else:
                if len(stack) == 0:
                    return False
                poped = stack.pop()
                if poped != hashMap[item]:
                    return False
        return len(stack) == 0
                    
