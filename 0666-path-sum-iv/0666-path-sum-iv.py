class Solution:
    def pathSum(self, nums: List[int]) -> int:
        coords_map = {}

        for num in nums:
            coordinates = num // 10
            value = num % 10
            coords_map[coordinates] = value

        total_sum = 0
        q = deque([(nums[0] // 10, coords_map[nums[0] // 10])])

        while q:
            coords, curr_sum = q.popleft()
            level = coords // 10
            position = coords % 10

            left_child = (level + 1) * 10 + position * 2 - 1
            right_child = (level + 1) * 10 + position * 2

            if not (left_child in coords_map or right_child in coords_map):
                total_sum += curr_sum

            if left_child in coords_map:
                q.append((left_child, curr_sum + coords_map[left_child]))

            if right_child in coords_map:
                q.append((right_child, curr_sum + coords_map[right_child]))

        return total_sum