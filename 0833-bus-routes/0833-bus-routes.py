class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        stop_to_bus = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_bus[stop].add(i)

        queue = deque([(source, 0)])
        visited_stops = set([source])
        visited_buses = set()

        while queue:
            stop, buses = queue.popleft()

            if stop == target:
                return buses

            for bus in stop_to_bus[stop]:
                if bus not in visited_buses:
                    visited_buses.add(bus)
                    for next_stop in routes[bus]:
                        if next_stop not in visited_stops:
                            visited_stops.add(next_stop)
                            queue.append((next_stop, buses + 1))

        return -1


        