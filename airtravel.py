

class Flight:

    def __init__(self, number):
        if not number[:2].isalpha():
            raise ValueError("no airline code in {}".format(number))
        if not number[:2].isupper():
            raise ValueError("invalid airline code {}".format(number))
        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError("invalid route number {}".format(number))
        self._number = number

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]
