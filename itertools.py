import itertools
'''
r = range(1, 10)
i = iter(r)
print(list(i))
print(next(i))
print(next(i))
print(next(i))

for i in range(1, 10):
    print(i)
'''


# INFINITE ITERTARATORS
'''
from itertools import count

def count_example(start, step):
    counter = count(start, step)

    for c in counter:
        print(c)

        if c == 100:
            break
count_example(10, 5)
'''

# TYPE 2 OF INFINITE ITERTARATORS
from itertools import repeat

def repeat_example(element, max_repeats):
    repeater = repeat(element, max_repeats)

    for val in repeater:
        print(val)

repeat_example("Hello World ", 25)