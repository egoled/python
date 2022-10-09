# class Balance:
#     right = 0
#     left = 0
#
#     def _init_(self):
#         self.right = 0
#         self.left = 0
#
#     def add_left(self, left):
#         self.left = left
#         print(self.left)
#
#     def add_right(self, right):
#         self.right = right
#         print(self.right)
#
#     def result(self):
#         if self.right == self.left:
#             print("=")
#         elif self.right < self.left:
#             print("L")
#         else:
#             print("R")
#
# b = Balance()
# b.add_left(3)
# b.add_right(4)
# b.result()

# class BigBell:
#     list_dong = ["ding", "dong"]
#     count = 0
#
#     def sound(self):
#         if self.count % 2 == 0:
#             print(self.list_dong[0])
#             self.count += 1
#         else:
#             print(self.list_dong[1])
#             self.count += 1
#
# bb = BigBell()
# bb.sound()
# bb.sound()
# bb.sound()

# class OddEvenSeparator:
#     even_list = []
#     odd_list = []
#
#     def add_number(self, num):
#         if num % 2 == 0:
#             self.even.append(num)
#         else:
#             self.odd.append(num)
#
#     def even(self):
#         return self.even
#
#     def odd(self):
#         return self.odd
#
# oes = OddEvenSeparator()
# oes.add_number(4)
# oes.add_number(1)
# oes.add_number(2)
# oes.add_number(6)
# oes.add_number(8)
#
# print(oes.even_list)
# print(oes.odd_list)

# class OddEvenSeparator:
#     even_list = []
#     odd_list = []
#
#     def add_number(self, num):
#         if num % 2 == 0:
#             self.even_list.append(num)
#         else:
#             self.odd_list.append(num)
#
#     def even(self):
#         return self.even
#
#     def odd(self):
#         return self.odd
#
# oes = OddEvenSeparator()
# oes.add_number(3)
# oes.add_number(8)
# oes.add_number(34)
# oes.add_number(1)
# oes.add_number(0)
# print(oes.even_list)
# print(oes.odd_list)

class MinMaxWordFinder:
    words = []
    num_dict = {}

    def add_sentence(self, text):
        text = str(text).split()
        for word in text:
            if len(word) in self.num_dict.keys():
                self.num_dict[len(word)]

    def short(self):
        min_w = len(self.words[0])
        for word in self.words:
            min_w =

    def long(self):
        return self.max

finder = MinMaxWordFinder()
finder.add_sentence("klkwvmd wef we k erw ew")
finder.add_sentence("jdgsnn jk sdf mklk ret")
print(finder.long())
print(finder.short())