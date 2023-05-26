class TrainTicket:
    def __init__(self, passenger_name, train_number, destination, departure_time, seat_number):
        self.passenger_name = passenger_name
        self.train_number = train_number
        self.destination = destination
        self.departure_time = departure_time
        self.seat_number = seat_number


class Train:
    def __init__(self, train_number, destination, departure_time, seats):
        self.train_number = train_number
        self.destination = destination
        self.departure_time = departure_time
        self.seats = seats

    def check_availability(self):
        return len(self.seats) > 0

    def book_seat(self):
        if not self.check_availability():
            return False
        else:
            seat_number = self.seats.pop(0)
            return seat_number


class TrainStation:
    def __init__(self):
        self.trains = []

    def add_train(self, train):
        self.trains.append(train)

    def buy_ticket(self, passenger_name, train_number):
        for train in self.trains:
            if train.train_number == train_number:
                if train.check_availability():
                    seat_number = train.book_seat()
                    ticket = TrainTicket(passenger_name, train_number, train.destination, train.departure_time, seat_number)
                    return ticket
                else:
                    return "Нет доступных мест по вашему запросу."
        return "Маршрут поезда не найден."


train1 = Train("123", "Novosibirsk", "10:00", [1, 2, 3])
station = TrainStation()
station.add_train(train1)


ticket1 = station.buy_ticket("Nikolay Razumovsky", "123")


print(f"Passenger: {ticket1.passenger_name}")
print(f"Train number: {ticket1.train_number}")
print(f"Destination: {ticket1.destination}")
print(f"Departure time: {ticket1.departure_time}")
print(f"Seat number: {ticket1.seat_number}")

