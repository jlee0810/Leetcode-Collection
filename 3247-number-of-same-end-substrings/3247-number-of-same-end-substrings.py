class Solution:
    def sameEndSubstringCount(self, s: str, queries: List[List[int]]) -> List[int]:
        char_counter = Counter()
        prefix_counters = [Counter()]

        for char in s:
            char_counter[char] += 1
            prefix_counters.append(char_counter.copy())

        def calculate_contribution(counter):
            return sum(count * (count + 1) // 2 for count in counter.values())

        results = []

        for left, right in queries:
            right_counter = prefix_counters[right + 1]
            left_counter = prefix_counters[left]
            
            substring_counter = right_counter - left_counter
            contribution = calculate_contribution(substring_counter)
            results.append(contribution)
        
        return results