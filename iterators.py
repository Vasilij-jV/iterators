# # -*- config: utf8 -*-
# import warnings
#
#
# class EvenNumbers:
#
#     def __init__(self, **kwargs):
#         if bool(kwargs) is not True:
#             self.start = 0
#             self.end = 1
#             warnings.warn(f'Слишком маленький диапазон между числом {self.start} и числом {self.end}')
#         elif ('start' in kwargs) is False and kwargs['end'] > 0:
#             self.start = 0
#             self.end = kwargs['end']
#         elif ('end' in kwargs) is False:
#             self.end = 1
#             self.start = 0
#             warnings.warn(f'Слишком маленький диапазон между числом {self.start} и числом {self.end}')
#         elif len(kwargs) == 2 and kwargs['start'] < kwargs['end']:
#             self.start = kwargs['start']
#             self.end = kwargs['end']
#             self.i = self.start
#
#     def __iter__(self):
#         self.i = self.start - 1
#         return self
#
#     def __next__(self):
#         self.i += 1
#         if self.i < self.end or self.i == self.end:
#             return self.i
#         else:
#             raise StopIteration
#
#
# en = EvenNumbers()
# for elem in en:
#     if elem % 2 == 0:
#         print(elem)

# -*- config: utf8 -*-
import warnings


class EvenNumbers:

    def __init__(self, **kwargs):
        # # Провeрка на наличие параметров
        # if bool(kwargs) is not True:
        #     self.start = 0
        #     self.end = 1
        #     warnings.warn(f'Слишком маленький диапазон между числом {self.start} и числом {self.end}')
        #
        # # Проверка на отсутствие одного из параметров
        # elif ('start' in kwargs) is False and kwargs['end'] > 0:
        #     self.start = 0
        #     self.end = kwargs['end']
        #     warnings.warn(f'Слишком маленький диапазон между числом {self.start} и числом {self.end}')
        #
        # # Проверка на отсутствие одного из параметров
        # elif ('start' in kwargs) is False and kwargs['end'] == 0:
        #     self.start = 0
        #     self.end = 1
        #     warnings.warn(f'Слишком маленький диапазон между числом {self.start} и числом {self.end}')
        #
        # # Проверка на отсутствие одного из параметров
        # elif ('end' in kwargs) is False:
        #     self.end = 1
        #     self.start = 0
        #     warnings.warn(f'Слишком маленький диапазон между числом {self.start} и числом {self.end}')
        #
        # # Проверка на значения параметров меньше допустимых
        # elif kwargs['start'] < 0 or kwargs['end'] < 1:
        #     self.end = 1
        #     self.start = 0
        #     warnings.warn(
        #         f'Слишком маленький диапазон между числом {self.start} и числом {self.end} или были введены отрицательные числа')
        #
        # # Проверка на равенство допустимых значений
        # elif kwargs['start'] == kwargs['end']:
        #     self.end = 1
        #     self.start = 0
        #     warnings.warn(f'Слишком маленький диапазон между числом {self.start} и числом {self.end}')

        # Проверка допустимых значений
        if len(kwargs) == 2 and kwargs['end'] > kwargs['start'] > -1 and kwargs['end'] > 1:
            self.start = kwargs['start']
            self.end = kwargs['end']
            self.i = self.start
        else:
            self.start = 0
            self.end = 1

    def __iter__(self):
        if self.start % 2 == 0:
            self.i = self.start - 2
        elif self.start % 2 != 0:
            self.i = self.start - 1
        return self

    def __next__(self):
        self.i += 2
        if self.i < self.end or self.i == self.end:
            return self.i
        else:
            raise StopIteration


en = EvenNumbers(start=0, end=50)
for elem in en:
    print(elem)
