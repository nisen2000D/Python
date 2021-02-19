class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f' Машина {self.name} {self.color} цвета поехала'

    def stop(self):
        return 'Машина остановилась'

    def turn(self, direction):
        return f'Поворот {direction}'

    def show_speed(self):
        return f'Скорость машины: {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'{self.name} превысила скорость. Скорость: {self.speed}'
        else:
            return f'Скорость нормальная. Скорость: {self.speed}'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Вы превысили скорость. Ваша скорость: {self.speed}'
        else:
            return f'Скорость нормальная. Ваша скорость: {self.speed}'


class PoliceCar(Car):
    pass


town_car = TownCar(80, 'чёрного', 'Lexus', False)
print(
    f'{town_car.go()},\n {town_car.show_speed()},\n {town_car.turn("налево")},\n {town_car.turn("направо")},\n {town_car.stop()}.')

sport_car = SportCar(60, 'белого', 'BMW', False)
print(
    f'{sport_car.go()},\n {sport_car.show_speed()},\n {sport_car.turn("направо")},\n {sport_car.turn("налево")},\n {sport_car.stop()}.')

work_car = WorkCar(30, 'зелёного', 'УАЗ', False)
print(
    f'{work_car.go()},\n {work_car.show_speed()},\n {work_car.turn("налево")},\n {work_car.turn("направо")},\n {work_car.stop()}.')

police_car = PoliceCar(60, 'чёрного', 'Mercedes-AMG', True)
print(
    f'{police_car.go()},\n {police_car.show_speed()},\n {police_car.turn("налево")},\n {police_car.turn("направо")},\n {police_car.stop()}.')
