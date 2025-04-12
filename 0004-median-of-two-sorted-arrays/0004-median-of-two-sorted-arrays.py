class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2

        # Ensure nums1 is the shorter array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        l, r = 0, len(nums1)  # Allow i to reach len(nums1) for boundary case

        while True:  # Use infinite loop with explicit return to handle all cases
            i = (l + r) // 2  # Partition point for nums1
            j = half - i      # Corrected formula for nums2 partition

            # Get left and right elements for both arrays
            n1_left = nums1[i - 1] if i > 0 else float("-inf")
            n1_right = nums1[i] if i < len(nums1) else float("inf")
            n2_left = nums2[j - 1] if j > 0 else float("-inf")
            n2_right = nums2[j] if j < len(nums2) else float("inf")

            # Check if partition is correct
            if n1_left <= n2_right and n2_left <= n1_right:
                # Handle even total length
                if total % 2 == 0:
                    return (max(n1_left, n2_left) + min(n1_right, n2_right)) / 2
                # Handle odd total length
                else:
                    return min(n1_right, n2_right)
            elif n1_left > n2_right:
                r = i - 1  # Move left in nums1
            else:
                l = i + 1  # Move right in nums1