# Lesson 9 dz 2 Smirnov Artem
class Road:
    def __init__(self, legth, width):
        self._legth = legth
        self._width = width

    def get_full_profit(self):
        return f"{self._legth} м *{self._width} м * 25 кг * 5 см = {(self._legth * self._width * 25 * 5) / 1000} т"


road_1 = Road(5000, 20)
print(road_1.get_full_profit())