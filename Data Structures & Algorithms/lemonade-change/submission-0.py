class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        billMap = {
            # 不找
            '5': 0,
            # 找5
            '10': 0,
        }

        for num in bills:
            if num == 5:
                billMap['5'] += 1
            elif num == 10:
                if billMap['5'] == 0:
                    return False
                billMap['10'] += 1
                billMap['5'] -= 1
            else:
                if billMap['10'] > 0 and billMap['5'] > 0:
                    billMap['10'] -= 1
                    billMap['5'] -= 1
                elif billMap['5'] >= 3:
                    billMap['5'] -= 3
                else:
                    return False
        return True     




