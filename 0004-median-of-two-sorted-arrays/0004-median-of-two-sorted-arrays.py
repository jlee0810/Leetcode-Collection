class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        l, r = 0, len(nums1) - 1

        while True:
            i = (l + r) // 2
            j = half - i - 2

            n1_left = nums1[i] if i >= 0 else float('-inf')
            n2_left = nums2[j] if j >= 0 else float('-inf')
            n1_right = nums1[i + 1] if i + 1 < len(nums1) else float('inf')
            n2_right = nums2[j + 1] if j + 1 < len(nums2) else float('inf')

            if n1_left <= n2_right and n2_left <= n1_right:
                if total % 2 == 0:
                    return (max(n1_left, n2_left) + min(n1_right, n2_right)) / 2
                else:
                    return min(n1_right, n2_right)
            elif n1_left > n2_right:
                r = i - 1
            else:
                l = i + 1