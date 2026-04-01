import bisect
class TimeMap:

    def __init__(self):
        self.memo = defaultdict(lambda: [])

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.memo[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.memo:
            return ""
        curr = self.memo[key]
        
        findIdx = bisect.bisect_right([time for time, v in curr], timestamp)-1
        return curr[findIdx][1] if findIdx != -1 else ""