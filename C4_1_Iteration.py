
'''
x = int(input("Find sum of numbers from 1 to: "))
y = 1
sum = 0
if y <= x:
    sum = sum + y
    y = y + 1
    print(sum)

# Reccursion in python 

def recursive_method(n):
    if n == 1:
        return 1 
    else:
        return n * recursive_method(n-1)
    # 5 * factorial_recursive(4)
    # 5 * 4 * factorial_recursive(3)
    # 5 * 4 * 3 * factorial_recursive(2)
    # 5 * 4 * 3 * 2 * factorial_recursive(1)
    # 5 * 4 * 3 * 2 * 1 = 120
num = int(input('enter num '))
print(recursive_method(num))
'''

x = 1
sum = 0
while x <= 10:
    sum = sum + x
    x = x + 1

print(sum)

#round is the name of a function, do not use it to calculate iteration "rounds"