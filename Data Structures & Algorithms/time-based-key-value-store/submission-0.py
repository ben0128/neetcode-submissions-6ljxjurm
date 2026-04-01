class TimeMap:

    def __init__(self):
        self.hashMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashMap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        tempLi = self.hashMap[key]
        if len(tempLi) == 0:
            return ''
        for item in tempLi[::-1]:
            if timestamp >= item[1]:
                return item[0]
        return ''

