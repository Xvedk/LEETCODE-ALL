import heapq

class SeatManager:
    def __init__(self, n):
        self.available_seats = list(range(1, n + 1))
        heapq.heapify(self.available_seats)
    def reserve(self):
        if self.available_seats:
            seat_to_reserve = heapq.heappop(self.available_seats)
            return seat_to_reserve
        return -1 
    def unreserve(self, seatNumber):
        heapq.heappush(self.available_seats, seatNumber)
