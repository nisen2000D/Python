import time


class TrafficLight:
    __color = ["\033[31m {}".format("Красный"), "\033[33m {}".format("Жёлтый"), "\033[32m {}".format("Зелёный")]

    def running(self):
        i = 0
        while i != 3:
            print(TrafficLight.__color[i])
            if i == 0:
                time.sleep(7)
            elif i == 1:
                time.sleep(2)
            elif i == 2:
                time.sleep(5)
            i += 1


a = TrafficLight
a.running(0)
