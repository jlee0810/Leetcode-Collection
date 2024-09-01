class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        
        def can_heat(radius):
            i = 0
            for heater in heaters:
                while i < len(houses) and heater - radius <= houses[i] <= heater + radius:
                    i += 1
                if i >= len(houses):
                    break
            return i == len(houses)
        
        l, r = 0, max(max(heaters) - min(houses), max(houses) - min(heaters))
        
        while l <= r:
            mid = (l + r) // 2
            if can_heat(mid):
                r = mid - 1
            else:
                l = mid + 1
        
        return l
