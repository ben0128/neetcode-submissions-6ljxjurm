class Solution:
    def hammingWeight(self, n: int) -> int:
        print(format(n, '032b'))
        li = [int(char) for char in str(format(n, '032b')) if char == '1']
        return len(li)