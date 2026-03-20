import random

def isEven(value) -> str:
    if value % 2 == 0:
        return "(even)"
    else:
        return "(odd)"

def dice() -> None:
    a = random.randint(1,6)
    print("Number:",a,isEven(a))

    return

dice()

    
    

