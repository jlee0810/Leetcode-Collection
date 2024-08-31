class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        stop_to_bus = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_bus[stop].add(i)

        q = deque([(source, 0)])
        visited_stops = set([source])
        visited_bus = set()

        while q:
            stop, bus_count = q.popleft()
            
            if stop == target:
                return bus_count
            
            for bus in stop_to_bus[stop]:
                if bus not in visited_bus:
                    visited_bus.add(bus)
                    for next_stop in routes[bus]:
                        if next_stop not in visited_stops:
                            visited_stops.add(next_stop)
                            q.append((next_stop, bus_count + 1))

        return -1
 