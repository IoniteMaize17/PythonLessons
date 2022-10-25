start = int(input("Enter starting position: "))
end = int(input("Enter ending position: "))

options = range(start,end)

for i in options:
    if i == 67:
        print("We found 67!")
        break
else:
    print("Seems that there was no answer in there.")