class Vehicle:
    __COLOR_VARIANTS = ['Зелёный', 'Голубой', 'Красный', 'Чёрный', 'Лиловый']

    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = str(owner)
        self.__model = str(__model)
        self.__engine_power = int(__engine_power)
        self.__color = str(__color)

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power} л.с.'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(f'{self.get_model()} \n{self.get_horsepower()} \n{self.get_color()} \nВладелец: {self.owner}')

    def set_color(self, new_color):
        self.new_color = str(new_color)
        flag_ = False
        for i in self.__COLOR_VARIANTS:
            if new_color.upper() == i.upper():
                self.__color = i
                flag_ = True
        if not flag_:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


v1 = Sedan('Егор', 'Лада Гранта', '400', 'зелёный')
v1.print_info()
v1.set_color('Pink')
v1.set_color('чЁРНЫЙ')
v1.owner = 'Барсик'
print()
v1.print_info()
