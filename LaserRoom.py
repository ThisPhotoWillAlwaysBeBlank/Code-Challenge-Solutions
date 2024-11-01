# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)

# numpy and scipy are available for use
import numpy
import scipy
import math
import bisect

length = get_number()
lasersACount = get_number()
lasersBCount = get_number()
sectors = 1
lasersA = []
lasersB = []
i = 0
while i < lasersACount:
    direction = get_word()
    value = get_number()
    if direction == 'R':
        value = value + length
    sectors = sectors + 1
    lasersA.append(value)
    i = i+1
lasersA.sort()
i = 0
while i < lasersBCount:
    direction = get_word()
    value = get_number()
    if direction == 'L':
        value = value - length
    j=0
    # pred = lambda lasersA: -1*lasersA
    # j = bisect.bisect_left(lasersA, value, key=pred)
    j = len(lasersA) - bisect.bisect_right(lasersA, value)
    # while(j<len(lasersA) and value<lasersA[j]):
    #      j = j+1

    sectors = sectors + j + 1
    i  = i +1
print(sectors)


