def printstuff(textline="Quack!"):
    print(textline)


# printstuff()


def printstuff(parameter1="First thing", parameter2="Second thing"):
    print(parameter1 + "------" + parameter2)


# printstuff()
# printstuff("d")
# You can call a function with 2 parameters and just give it 1 value.
# It will return the given value to the first parameter and default the second.
def printstuff(value=12, parameter1="First thing", parameter2="Second thing"):
    print(parameter1 + "------" + parameter2)
    print(value)


# printstuff()


def square(width=float(5.0), height=float(8.0)):
    area = width * height
    return area


'''def main():
    # we can leave some parameters out
    # because now we have default values
    area1 = square()
    area2 = square(4.0, 3.0)
    area3 = square(10.0)
    area4 = square(height=11.0)

    print("Four different ways of calling our function...")
    print("And they all work:")
    print(area1, area2, area3, area4)'''


'''if __name__ == "__main__":
    main()'''
