class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # aab
        
        # a  => ['a']

        # a a => [['a', 'a'], ['aa']]

        # a a b => [['a', 'a', 'b'], ['aa', 'b']]
        
        # a a b a => ['a', 'a', 'b', 'a'], ['aa', 'b', 'a']
        # current situation = prev + (1 if current word is palindrome else 0)

        memo = []
        n = len(s)
        def backtracing(i, j, tmp):
            if s[i:j] != s[i:j][::-1]:
                return
            tmp.append(s[i:j])
            if j == n:
                memo.append(tmp.copy())
                tmp.pop()
                return
            for k in range(j+1, n+1):
                backtracing(j, k, tmp)
            tmp.pop()

        for end in range(1, n+1):
            backtracing(0, end, [])
        return memo