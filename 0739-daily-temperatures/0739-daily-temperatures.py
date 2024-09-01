class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mono_stack = [(temperatures[0], 0)]
        result = [0 for _ in range(len(temperatures))]

        for i in range(1, len(temperatures)):
            while mono_stack and temperatures[i] > mono_stack[-1][0]:
                _, prev_idx = mono_stack.pop()
                result[prev_idx] = i - prev_idx
            mono_stack.append((temperatures[i], i))

        return result