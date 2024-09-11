class SeatManager:

    def __init__(self, n: int):
        self.avail = []
        for i in range(1, n + 1):
            self.avail.append(i)

    def reserve(self) -> int:
        smallest_seat = heappop(self.avail)
        return smallest_seat

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.avail, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)