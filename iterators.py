class EvenNumbers:

    def __init__(self, **kwargs):

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
