class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        record = [1] * n

        for i in range(1, m):
            tmp = [0] * n
            for j in range(n):
                tmp[j] = record[j]
                if j-1 >= 0:
                    tmp[j] += tmp[j-1]
            
            record = tmp
        print(record)
        return record[-1]
