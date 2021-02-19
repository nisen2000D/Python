class Road:
    def __init__(self, width, length):
        self._length = length
        self._width = width
        self.weight = 25
        self.thickness = 5

    def mass_asphalt(self):
        mass = self._length * self._width * self.weight * self.thickness
        ton = mass / 1000
        print(int(ton))


r = Road(20, 5000)
r.mass_asphalt()
