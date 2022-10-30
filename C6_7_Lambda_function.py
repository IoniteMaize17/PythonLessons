def adder(n):
    return lambda total: total + n

bigadder = adder(5)
result = bigadder(10)
print(result)