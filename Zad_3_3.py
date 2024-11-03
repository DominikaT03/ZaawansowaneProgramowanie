class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"{self.area} m2, {self.rooms} pokoi, {self.price} zł, Adres: {self.address}"


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"Dom: {super().__str__()}, Rozmiar działki: {self.plot} m2"


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"Mieszkanie: {super().__str__()}, Piętro: {self.floor}"


house = House(200, 5, 500000, "1 Maja 30, Katowice", 800)
flat = Flat(80, 3, 300000, "Chorzowska 100, Katowice", 5)

print(house)
print(flat)