class Date:
    def __init__(self, str_date):
        self.str_date = str_date

    @classmethod
    def transform_num(cls, str_date):
        date = str_date.split('-')
        day = int(date[0])
        month = int(date[1])
        year = int(date[2])
        return day, month, year

    @staticmethod
    def check(str_date):
        day, month, year = map(int, str_date.split('-'))
        if day < 31 and day > 1:
            if month < 12 and month > 1:
                if year < 2020 and year > 0:
                    print('Дата введена правильно')
                else:
                    print('Год не может быть меньше 0 или больше 2020')
            else:
                print('Месяц не может быть меньше 1 или больше 12')
        else:
            print('Число не может быть меньше 1 или больше 31')


date = '17-8-2000'
data_obj = Date(date)
int_date = data_obj.transform_num(date)
print(int_date)
print(type(int_date[0]))
check = Date.check(date)
