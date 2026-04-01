class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        maxTime = -1
        count = 0
        for pos, sp in sorted(zip(position, speed), reverse=True):
            currTime = (target-pos)/sp
            if maxTime < currTime:
                count += 1
                maxTime = currTime
        return count