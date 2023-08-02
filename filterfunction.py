def isAOne(x):
    return x == 1

nums = [1,1,6,7,8,0,1,1]

newList = list(filter(isAOne,nums))

# newList is [1,1,1,1]