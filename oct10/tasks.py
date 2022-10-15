# class foodInfo:
#
#     def __init__ (self, proteins, fets, carbohydrates):
#         self.proteins = proteins
#         self.fats = fats
#         self.carbohydrates = carbohydrates
#
#     def get_proteins (self):
#         return self.get_proteins
#
#     def get_fats (self):
#         return self.fats
#
#     def get_carbohydrates (self):
#         return self.carbohydrates
#
#     def get_calories (self):
#         return 4*self.proteins + 9*self.fats + 4*self.carbohydrates
#
#     def __add__ (self, other):
#         return foodInfo(self.proteins + other.proteins, self.fats + other.fats, self.carbohydrates + other.carbohydrates)
#
#     food1 = foodInfo(100, 100, 100)
#     food2 = foodInfo(50, 60, 70)


# class ReversedList:
#     def __init__ (self, some_list):
#         self.some_list = some_list
#
#     def __getitem__ (self, index):
#         return self.some_list[-index]
#
#     def __len__ (self):
#         return len(self.some_list)
#
# ri = ReversedList([])
# for i in range (len(ri)):
#  print (len(ri))

# class Date:
#
#     def __init__(self, m, d):
#         self.m = m
#         self.d = d

class Date:
    def __init__ (self, month, day):
        self.month = month
        self.day = day

    def __sub__(self, other):
        day1 = dt.date(2021, self.month, self.day)
        day2 = dt.date(2021, other.month, other.day)
        return dt.datetime(day1 - day2)

