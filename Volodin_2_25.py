x = int(input())
maximum = 0
previous = 0
while x != 0:
    if x > maximum:
        previous = maximum
        maximum = x
    elif x > previous and x < maximum:
        previous = x
    x = int(input())
print(previous)