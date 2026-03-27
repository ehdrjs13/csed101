def program1() -> None:
    for i in range(10):
        print(10-i, end=", ")
    print("Happy new year!!")

program1()

def program2(value:str) -> None:
    for i in range(len(value)):
        print(value[len(value)-i-1],end="")

program2("12345")
print()

def program3(value:str) -> int:
    sum = 0
    for i in value:
        sum += int(i)
    
    return sum

print(program3("13452"))
        