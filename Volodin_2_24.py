x = int(input())
y = 0
z = 0
while x != 0:
    y = int(input())
    if y > x:
        z += 1
    x = y
print(z)
