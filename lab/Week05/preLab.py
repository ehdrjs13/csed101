def gugudan(num:int) -> None:
    for i in range(9):
        print(f"{num} * {i+1} = {num*(i+1)}")

number = int(input("Engter a table number:"))

gugudan(number)