# import time
# class TrafficLight:
#     color = 'red'
#
#     def running(self):
#         print(TrafficLight.color)
#         time.sleep(7)
#         print('yellow')
#         time.sleep(3)
#         print('green')
#         time.sleep(5)
#
# tr = TrafficLight()
# tr.running()

# class Road:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def func (self, weight, height):
#         return self.length * self.width * weight * height / 1000
#
# a = Road(100, 20)
# print (a.func(20, 20))

# class Auto:
#     def __init__ (self):
#         print('Автомобиль заведен')
#         self.auto_name = 'Mazda'
#         self._auto_year = 2019
#         self.__auto_model = 'CX9'
#
# a = Auto()
# print(a.auto_name)

# class MyClass:
#     __attr = "значение"
#
#     def __method(self):
#         print("Это защищенный метод!")
#
# mc1 = MyClass()
# mc1._MyClass__method()

# class Transport:
#     def transport_method(self):
#             print("Это родительский метод из класса Transport")
#     # Класс Auto, наследующий Transport
#
# class Auto(Transport):
#     def auto_method(self):
#          print("Это метод из дочернего класса")
#
# a = Auto()
# a.transport_method()

# class Shape:
#     def __init__(self, color, param_1, param_2):
#         self.color = color
#         self.param_1 = param_1
#         self.param_2 = param_2
#     def square(self):
#         return self.param_1 * self.param_2
#
# class Rectangle(Shape):
#     def __init__(self, color, param_1, param_2, rectangle_p):
#         super().__init__(color, param_1, param_2)
#         self.rectangle_p = rectangle_p
#     def get_r_p(self):
#         return self.rectangle_p
#
# class Triangle(Shape):
#     def __init__(self, color, param_1, param_2, triangle_p):
#         super().__init__(color, param_1, param_2)
#         self.triangle_p = triangle_p
#     def get_t_p(self):
#         return self.triangle_p
#
# r = Rectangle("white", 10, 20, True)
# print(r.color)
# print(r.square())
# print(r.get_r_p())
# t = Triangle("red", 30, 40, False)
# print(t.color)
# print(t.square())
# print(t.get_t_p())

# class Player:
#     def first_method(self):
#         print("Родительский метод класса Player")
#
# class Navigator:
#     def first_method(self):
#         print("Родительский метод класса Navigator")
#
# class MobilePhone(Player, Navigator):
#     def mobile_phone_method(self):
#         print("Дочерний метод класса MobilePhone")
#
# a = MobilePhone()
# a.first_method()

class Person:
    def __init__ (self, name, surname, second_name, dict_ph):
        self.name = name
        self.second_name = second_name
        self.surname = surname
        self.dict_ph = dict_ph

    def get_name(self):
        return self.name

    def get_phone(self):
        return dict(self.dict_ph).get('private')

    def get_work_phone(self):
        return dict(self.dict_ph).get('work')

    def get_sms_text(self):
        return f'Уважаемый {self.name}{self.surname}! Примите участие в конкурсе!'

class Company:
    def __init__ (self, name_c, type_c, dict_c, *person):
        self.name_c = name_c
        self.type_c = type_c
        self.dict_c = dict_c
        self.person_list = list(person)

    def get_phone(self):
        if self.dict_c.get('contact'):
            return self.dict_c.get('contact')
        else:
            print (Person(self.person_list[0]).get_phone())

    def get_name(self):

    def get_sms_text(self):

a = Person ('a', 'v', 'a', {'private': 1234, 'work': 5678})
print (a.get_name())
print (a.get_phone())
print (a.get_work_phone())
print(a.get_sms_text())

# class Company: