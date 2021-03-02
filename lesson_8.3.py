class MyList:
    def __init__(self, *args):
        self.user_list = []

    def test(self):
        while True:
            try:
                user = int(input('Введите список: '))
                self.user_list.append(user)
                print(self.user_list)
            except:
                print('Нужно ввести число')
                user2 = input('Введите список. Для выхода нажмите "q". Чтобы продолжить "r"')

                if user2 == 'q' or user2 == 'Q':
                    print(self.user_list)
                    return 'Выход'

                elif user2 == 'r' or user2 == 'R':
                    print(my_list.test())
                else:
                    return 'Выход'



my_list = MyList(1)
print(my_list.test())
