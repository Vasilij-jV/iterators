# -*- config: utf8 -*-

def fun(text):
    beginning = 0
    end = 1

    while True:
        if end == len(text) + 1:
            end = end - beginning + 1
            beginning = 0
        if (end - beginning) == len(text) + 1:
            break
        yield text[beginning:end]
        beginning += 1
        end += 1


f = fun('generator')
len_substring = 0
for signs in f:
    print(signs)
