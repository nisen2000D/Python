class Zero:
    def __init__(self, dividend, divider):
        self.dividend = dividend
        self.divider = divider

    @staticmethod
    def division(dividend, divider):
        try:
            return round(dividend / divider, 2)
        except ZeroDivisionError:
            return 'Делить на ноль нельзя'


zero = Zero
print(zero.division(2, 0))
print(zero.division(10, 3))
