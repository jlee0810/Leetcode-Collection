class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        money_dict = defaultdict(int)
        for bill in bills:
            money_dict[bill] += 1
            if bill == 5:
                continue
            if bill == 10:
                if money_dict[5] == 0:
                    return False
                else:
                    money_dict[5] -= 1
            if bill == 20:
                if money_dict[10] == 0:
                    if money_dict[5] < 3:
                        return False
                    money_dict[5] -= 3
                else:
                    if money_dict[5] < 1:
                        return False
                    money_dict[10] -= 1
                    money_dict[5] -= 1

        
        return True