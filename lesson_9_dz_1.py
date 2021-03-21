# Lesson 9 dz 1 Smirnov Artem


from time import sleep


class TrafficLight:
    __color = "Черный"

    def running(self):
        while True:
            print("RED")
            sleep(7)
            print("YELLOW")
            sleep(2)
            print("GREEN")
            sleep(7)
            print("YELLOW")
            sleep(2)


traficlight = TrafficLight()
traficlight.running()


