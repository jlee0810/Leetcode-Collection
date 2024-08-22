class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ratio_dict = defaultdict(int)

        for width, height in rectangles:
            ratio = width / height
            ratio_dict[ratio] += 1
            
        result = 0

        for count in ratio_dict.values():
            if count > 1:
                result += count * (count - 1) // 2
        
        return result
