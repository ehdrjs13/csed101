def mulTable() -> None:
    for y in range(1,10):
        for x in range(1,10):
            print(f"{x} * {y} = {x*y}", end="\t")
        print()
        

    return

mulTable()

def starPattern(value: int) -> None:
    for num in str(value):
        for i in range(int(num)):
            print("별",end=" ")
        print()

    print()

    return

starPattern(12345)
