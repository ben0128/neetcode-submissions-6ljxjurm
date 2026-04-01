class TimeMap:

    def __init__(self):
        self.hashMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashMap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        tempLi = self.hashMap[key]
        left, right = 0, len(tempLi)-1
        res = -1
        while left <= right:
            mid = left + (right-left)//2
            if tempLi[mid][1] <= timestamp:
                res = mid
                left = mid+1
            else:
                right = mid - 1
        return tempLi[res][0] if res != -1 else ''

