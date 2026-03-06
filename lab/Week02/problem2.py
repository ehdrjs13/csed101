def makeChange(value) -> list:
    five = value // 500
    value = value % 500
    
    one = value // 100

    return [five,one]

money = int(input("Money inserted:"))
price = int(input("Item price:"))

change = money - price
res = makeChange(change)

print("Change: ", change)
print("500-won coins:",res[0])
print("100-won coins:",res[1])
