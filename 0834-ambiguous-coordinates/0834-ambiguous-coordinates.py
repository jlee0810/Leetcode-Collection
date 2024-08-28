class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        nums = s[1:-1]

        def place_period(s):
            if s[0] == '0':
                if len(s) > 1:
                    if s[-1] == '0':
                        return set()
                    else:
                        return set([f'0.{s[1:]}'])
                else:
                    return set(['0'])
            else:
                produced = set([s])
                if s[-1] != '0':
                    for i in range(1, len(s)):
                        left = s[:i]
                        right = s[i:]
                        produced.add(left+'.'+right)
                return produced
        
        res = []

        for i in range(1, len(nums)):
            first_half, second_half = nums[:i], nums[i:]

            left_produced = place_period(first_half)
            right_produced = place_period(second_half)
            for left_val in left_produced:
                for right_val in right_produced:
                    res.append(f'({left_val}, {right_val})')
        return res