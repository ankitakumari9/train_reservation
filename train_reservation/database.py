class Database:
    def __init__(self):
        # Initial seat status (example with some seats already booked)
        self.seats = [False] * 80
        self.seats[0] = True  # Example of an already booked seat
        self.seats[10] = True # Another already booked seat
        # ... Initialize other seats as needed

    def get_seat_status(self):
        return self.seats

    def check_availability(self, num_seats):
        for i in range(12):
            if i < 11:
                for j in range(7 - num_seats + 1):
                    if all(not self.seats[i * 7 + j + k] for k in range(num_seats)):
                        return (i, j)
            else:
                if num_seats <= 3 and all(not self.seats[77 + k] for k in range(num_seats)):
                    return (11, 0)
        return None

    def reserve_seats(self, num_seats):
        available = self.check_availability(num_seats)
        if available:
            row, start = available
            for k in range(num_seats):
                if row < 11:
                    self.seats[row * 7 + start + k] = True
                else:
                    self.seats[77 + k] = True
            return True
        return False
