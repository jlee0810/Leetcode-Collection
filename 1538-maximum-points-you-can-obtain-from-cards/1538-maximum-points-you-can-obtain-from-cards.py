class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        
        front = [0] * (k + 1)
        back = [0] * (k + 1)
        
        for i in range(1, k + 1):
            front[i] = front[i - 1] + cardPoints[i - 1]
        
        for i in range(1, k + 1):
            back[i] = back[i - 1] + cardPoints[n - i]
        
        max_score = 0
        for i in range(k + 1):
            max_score = max(max_score, front[i] + back[k - i])
        
        return max_score
