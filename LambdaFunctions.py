func = lambda x: x+5

print(func(2))
# Prints 7

func = lambda x, y: x+y

print(func(2,2))
# Prints 4

myList = [1,4,6,7,8,11,3,4,6]

#newList = list(filter(lambda x: return x > 5, myList))
# newList is [6,7,8,11,6]

newList2 = list(map(lambda x: x+1, myList))
# newList 2 is [2,5,7,8,9,12,4,5,7]