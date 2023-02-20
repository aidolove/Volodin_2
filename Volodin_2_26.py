x = int(input())
maximum = 0
quantity = 0
while x != 0:
    if x > maximum:
        maximum = x
        quantity = 1
    elif x == maximum:
        quantity += 1  
    x = int(input())
print(quantity)
