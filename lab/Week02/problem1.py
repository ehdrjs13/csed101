def separate(date) -> list:
    year, month, day = date.split("-")
    
    year = int(year) + 10

    return [year,month,day]

date = input("Enter a date (YYYY-MM-DD):")

result = separate(date)
print("The date 10 years later is", f"{result[0]}-{result[1]}-{result[2]}")
