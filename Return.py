def averege(*numbers):
    for i in numbers:
        sum = 0
        sum = sum + i
        return sum/len(numbers)
c = averege(6,8,10,15)
print(c)
