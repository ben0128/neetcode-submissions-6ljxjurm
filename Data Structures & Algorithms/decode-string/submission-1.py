class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)
        def recursive(idx):
            num = 0
            word = ''
            # for k, c in enumerate(s[idx:], idx):
            while idx < n:
                c = s[idx]
                if c.isdigit():
                    num = num*10 + int(c)
                elif c == '[':
                    tmpWord, nxtIdx = recursive(idx+1)
                    word = word + tmpWord*num
                    idx, num = nxtIdx, 0
                elif c == ']':
                    return [word, idx]
                else:
                    word += c
                idx += 1
            return word
        return recursive(0)