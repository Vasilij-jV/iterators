# -*- config: utf8 -*-
import warnings


class EvenNumbers:

    def __init__(self, **kwargs):
        if bool(kwargs) is not True:
            self.start = 0
            self.end = 1
            warnings.warn(f'Слишком маленький диапазон между числом {self.start} и числом {self.end}')
        elif ('start' in kwargs) is False and kwargs['end'] > 0:
            self.start = 0
            self.end = kwargs['end']
        elif ('end' in kwargs) is False:
            self.end = 1
            self.start = 0
            warnings.warn(f'Слишком маленький диапазон между числом {self.start} и числом {self.end}')
        elif len(kwargs) == 2 and kwargs['start'] < kwargs['end']:
            self.start = kwargs['start']
            self.end = kwargs['end']
            self.i = self.start

    def __iter__(self):
        self.i = self.start - 1
        return self

    def __next__(self):
        self.i += 1
        if self.i < self.end or self.i == self.end:
            return self.i
        else:
            raise StopIteration


en = EvenNumbers()
for elem in en:
    if elem % 2 == 0:
        print(elem)
