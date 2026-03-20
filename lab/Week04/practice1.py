def maxValue(a,b,c) -> int:
    if a > b and a > c: 
        return a
    elif b > c:
        return b
    else:
        return c
    
a,b,c = input("Enter three numbers:").split()

print(f"The largest number is {maxValue(int(a), int(b), int(c))}")

