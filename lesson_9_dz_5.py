# Lesson 9 dz 5 Smirnov Artem

class Stationery:
    def __init__(self, title = "Somethinf that can draw"):
        self.title = title

    def draw(self):
        print(f"Just start drawing! {self.title}")


class Pen(Stationery):
    def draw(self):
        print(f"Start drawing with {self.title} pen!")


class Pecil(Stationery):
    def draw(self):
        print(f"Start drawing with {self.title} pencil!")


class Marker(Stationery):
    def draw(self):
        print(f"Start drawing with {self.title} marker!")


stat = Stationery()
stat.draw()
pen = Pen("Stabilo PointVisco")
pen.draw()
pencil = Pecil("Cross")
pencil.draw()
marker = Marker("Centropen")
marker.draw()