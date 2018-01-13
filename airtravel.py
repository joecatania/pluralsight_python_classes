''' test test comment '''

class Flight:

    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError("no airline code in {}".format(number))
        if not number[:2].isupper():
            raise ValueError("invalid airline code {}".format(number))
        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError("invalid route number {}".format(number))
        self._number = number
        self._aircraft = aircraft

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def aircraft_model(self):
        return self._aircraft.model()

class Aircraft:

    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seating_plan(self):
        return (range(1, self._num_rows + 1),
                "abcdefghijk"[:self._num_seats_per_row])
