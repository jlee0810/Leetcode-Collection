class Solution:        
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        def rotate(num):
            rotate_A = rotate_B = 0
            for i in range(len(A)):
                if A[i] != num and B[i] != num:
                    return -1
                elif A[i] != num and B[i] == num:
                    rotate_A += 1
                elif A[i] == num and B[i] != num:
                    rotate_B += 1
            return min(rotate_A, rotate_B)
        
        sameA0 = rotate(A[0])
        
        if sameA0 == -1:
            return rotate(B[0])
        else:
            return sameA0