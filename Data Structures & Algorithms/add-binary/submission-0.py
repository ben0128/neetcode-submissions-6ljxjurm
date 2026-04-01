class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        res = 0
        la, lb = len(a)-1, len(b)-1
        isAdd = False
        i = 0
        while la >= 0 or lb >= 0 or isAdd:
            tmp = 1 if isAdd else 0
            if la >= 0:
                tmp += int(a[la])
                la -= 1
            if lb >= 0:
                tmp += int(b[lb])
                lb -= 1
            
            isAdd = False

            if tmp//2 == 1 and tmp % 2 == 1:
                isAdd = True
                res |= 1 << i
            elif tmp//2 == 1 and tmp % 2 == 0:
                isAdd = True
            elif tmp%2 == 1:
                res |= 1 << i
            i += 1
            print(bin(res))
        return str(bin(res))[2:]
